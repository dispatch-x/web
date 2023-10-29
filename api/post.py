import sqlite3, json, datetime
from checkuser import check
from uuid import uuid4
import envkeys
from replit import db
import requests


def contains_profanity(text):
  api_url = f"http://www.purgomalum.com/service/containsprofanity?text={text}"
  response = requests.get(api_url)
  return response.json()


def post(current_user: str, room_uuid: str, msg: str):
  if contains_profanity(msg):
    return {"message": "contains_profanity", "code": 422}
  uuid = str(uuid4())
  connection = sqlite3.connect("dispatchx")
  connection.execute(
    "CREATE TABLE IF NOT EXISTS messages (message_uuid STRING, room_uuid STRING, sender STRING, content STRING, sent INT);"
  )
  cursor_object = connection.execute("SELECT * FROM rooms")
  ret = []
  retup = ()
  for tup in cursor_object.fetchall():
    ret += [tup[0]]
  if room_uuid not in ret:
    return {
      "code": 404,
      "uuid": "badroomuuiderror",
    }
  encoded_msg = envkeys.encrypt(
    msg, envkeys.string_to_key(envkeys.retrieve(room_uuid)))
  encoded_sender = envkeys.encrypt(
    current_user, envkeys.string_to_key(envkeys.retrieve(room_uuid)))
  # print(encoded_msg)
  # print(
  #   f"INSERT INTO messages (message_uuid, room_uuid, sender, content) VALUES ('{uuid}', '{room_uuid}', '{current_user}', '{encoded_msg}')"
  # )
  connection.execute(
    f"INSERT INTO messages (message_uuid, room_uuid, sender, content, sent) VALUES ('{uuid}', '{room_uuid}', '{encoded_sender}', '{encoded_msg}', {int(datetime.datetime.utcnow().timestamp())})"
  )
  connection.commit()
  connection.close()
  return {"code": 200, "uuid": uuid}


def list_room_messages(room_uuid: str, username, timestamp=0) -> list:
  print(room_uuid)
  connection = sqlite3.connect("dispatchx")
  res = connection.execute(f"SELECT * FROM rooms WHERE uuid='{room_uuid}'")
  toload = res.fetchall()
  print(toload[0][1])
  reslist = toload[0][1]
  print(
    envkeys.decrypt(reslist,
                    envkeys.string_to_key(envkeys.retrieve(room_uuid))))

  if username not in eval(
      envkeys.decrypt(reslist,
                      envkeys.string_to_key(envkeys.retrieve(room_uuid)))):
    return {"code": 401, "message": "bad_user_error"}
  cursor_object = connection.execute(
    f"SELECT * FROM messages WHERE room_uuid='{room_uuid}' AND sent>{timestamp}"
  )
  ret = []
  for tup in cursor_object.fetchall():
    print(tup[3])
    ret += [{
      "message_uuid":
      tup[0],
      "room_uuid":
      tup[1],
      "sender":
      envkeys.decrypt(tup[2],
                      envkeys.string_to_key(envkeys.retrieve(room_uuid))),
      "content":
      envkeys.decrypt(tup[3],
                      envkeys.string_to_key(envkeys.retrieve(room_uuid))),
      "sent":
      tup[4]
    }]
  return {"code": 200, "content": ret}
