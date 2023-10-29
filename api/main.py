from flask import Flask, request, abort, render_template
import post
import createRoom
import json
import admins
import user_pass
from replit import db
import secrets

app = Flask(__name__)

from werkzeug.exceptions import HTTPException


@app.errorhandler(HTTPException)
def handle_exception(e):
  """Return JSON instead of HTML for HTTP errors."""
  # start with the correct headers and status code from the error
  response = e.get_response()
  # replace the body with JSON
  response.data = json.dumps({
    "code": e.code,
    "name": e.name,
    "description": e.description,
  })
  response.content_type = "application/json"
  return response


autherror = json.dumps({"message": "failed_oauth_key", "code": 401})
# ^ returned when the oauth_key is wrong

methoderror = lambda: json.dumps({
  "message": f"we wanted GET but got {request.method}",
  "code": 405
})
# ^ returned when we don't have GET
"""
How do docstrings work in this piece of code:

@desc
Short description of the function.
@path_params
Any parameters specified in the path.
@url_params
Any parameters sent after the ?

Example
\"""
@app.route('/api/v2/user/<user>/auth')
...
@desc
Returns a true or false value based on if the oauth_key is correct
@path_params
`user` - the user that we are checking
@url_params
`oauth_key` - the expected oauth_key 
\"""

An example url string would be /api/v2/test1/auth?oauth_key=test2
"""


@app.route('/')
def index():
  """
  Returns a little joke for all those who have sat an exam
  """
  return render_template("leftblank.html"), 200


@app.route('/api/v2/user/<user>/auth')
def auth_url(user):
  """
  @desc
  Returns a true or false value based on if the oauth_key is correct
  @path_params
  `user` - the user that we are checking
  @url_params
  `password` - the expected password 
  """
  if request.method == 'GET':
    print(request)
    if user_pass.matches(user, request.args.get('password')) == True:
      oauth_key = secrets.token_urlsafe(32)
      db[f'{user}_oauth_key'] = oauth_key
      return {"code": 200, "key": oauth_key}
    else:
      return autherror
  else:
    return methoderror()


def auth(user, oauth):
  """
  Helper function for authentication internally (no API route)
  """
  return db[f'{user}_oauth_key'] == oauth


@app.route('/api/v2/rooms/<room_uuid>/post')
def postmsg(room_uuid):
  """
  @desc
  Posts a message to a room
  @path_params
  `room_uuid` - the uuid of the room where the message shall reside
  @url_params
  `user` - username
  `oauth_key` - oauth_key to check
  `msg` - message to post
  """
  if request.method == 'GET':
    if auth(request.args.get('user'), request.args.get('oauth_key')):
      return json.dumps(
        post.post(request.args.get('user'), room_uuid,
                  request.args.get('msg')))
    else:
      return autherror
  else:
    return methoderror()


@app.route('/api/v2/rooms/<room_uuid>/messages')
def listroom(room_uuid):
  """
  @desc
  Lists all messages for a room
  @path_params
  `room_uuid` - the uuid of the room that we wish to grab messages from
  @url_params
  `user` - username
  `oauth_key` - oauth_key to check
  `timestamp` - list all messages after this point (default 0)
  """
  if request.method == 'GET':
    if auth(request.args.get('user'), request.args.get('oauth_key')):
      if "timestamp" in request.args:
        ts = request.args.get("timestamp")
      else:
        ts = 0
      return json.dumps(
        post.list_room_messages(room_uuid, request.args.get('user'), ts))
    else:
      return autherror
  else:
    return methoderror()


@app.route('/api/v2/rooms/create')
def newroom():
  """
  @desc
  Creates a new room
  @url_params
  `user` - username
  `oauth_key` - oauth_key to check
  `alias` - what the room shall be nicknamed
  `users` - a comma-seperated list of the members 
  Note - not all members specified have to currently exist
  """
  if request.method == 'GET':
    if auth(request.args.get('user'), request.args.get('oauth_key')):
      return json.dumps(
        createRoom.createRoom(
          request.args.get('users').split(","), request.args.get('alias'),
          request.args.get('user')))
    else:
      return autherror
  else:
    return methoderror()


@app.route('/api/beta/user/<user>/delete')
def deluser(user):
  """
  NOTE: This endpoint is in ALPHA testing, and may never come out, I am still deciding
  
  @desc
  Deletes the current user
  @path_params
  `user` - username
  @url_params
  `oauth_key` - oauth_key to be checked
  """
  if request.method == 'GET':
    if auth(user, request.args.get('oauth_key')):
      return json.dumps(user_pass.delete_user(user))
    else:
      return autherror


@app.route('/api/v2/user/<user>/rooms')
def listroom2(user):
  """
  @desc
  Lists all rooms a user is in
  @path_params
  `user` - username
  @url_params
  `oauth_key` - oauth_key to be checked
  """
  if request.method == 'GET':
    if auth(user, request.args.get('oauth_key')):
      return json.dumps(createRoom.list_user_rooms(user))
    else:
      return autherror
  else:
    return methoderror()


@app.route('/api/v2/user/<user>')
def userinfo(user):
  """
  @desc
  Provides the info from the db on given user
  @path_params
  `user` - user to search
  """
  return json.dumps(user_pass.user(user))


@app.route('/api/v2/user/<user>/status')
def status(user):
  """
  @desc
  Sets a user's status
  """
  if request.method == 'GET':
    if auth(user, request.args.get('oauth_key')):
      return json.dumps(user_pass.set_status(user, request.args.get('status')))
    else:
      return autherror
  else:
    return methoderror()


@app.route('/api/v2/users/all')
def usersall():
  """
  @desc
  Lists all users
  @url_params
  `user` - username
  `oauth_key` - oauth_key to be checked
  """
  if request.method == 'GET':
    if auth(request.args.get('user'), request.args.get('oauth_key')):
      return json.dumps(user_pass.list_users(request.args.get('user')))
    else:
      return autherror
  else:
    return methoderror()


@app.route('/api/v2/users/new')
def new_user():
  """
  @desc
  Creates a new user
  @url_params
  `user` - username
  `oauth_key` - oauth_key of proposed user
  """
  if request.method == 'GET':
    return json.dumps(
      user_pass.new_user(request.args.get('user'),
                         request.args.get('oauth_key')))
  else:
    return methoderror()


app.run(host='0.0.0.0', port=81)
