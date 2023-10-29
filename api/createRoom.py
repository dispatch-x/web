from uuid import uuid4
import sqlite3, os, requests
from checkuser import check
import envkeys


def generate_symmetric_key():
  # Generate a 32-byte (256-bit) random key
  key = os.urandom(32)
  return key


def contains_profanity(text):
  api_url = f"http://www.purgomalum.com/service/containsprofanity?text={text}"
  response = requests.get(api_url)
  return response.json()


def createRoom(users: list[str], alias: str, current_user: str):
  # new room, users allowed `users`, alias `alias`, also please fill in `current_user`. returns
  uuid = str(uuid4())
  envkeys.generate(uuid)
  if contains_profanity(str(users)) or contains_profanity(alias):
    return {"message": "contains_profanity", "code": 422}
  user = current_user
  connection = sqlite3.connect("dispatchx")
  connection.execute(
    "CREATE TABLE IF NOT EXISTS rooms (uuid STRING, usersdump STRING, alias STRING, creator STRING);"
  )
  encoded_users = envkeys.encrypt(
    str(users), envkeys.string_to_key(envkeys.retrieve(uuid)))
  encoded_creator = envkeys.encrypt(
    user, envkeys.string_to_key(envkeys.retrieve(uuid)))
  encoded_alias = envkeys.encrypt(
    alias, envkeys.string_to_key(envkeys.retrieve(uuid)))
  connection.execute(
    f'INSERT INTO rooms (uuid, usersdump, alias, creator) VALUES (\'{uuid}\', "{encoded_users}", \'{encoded_alias}\', \'{encoded_creator}\')'
  )
  connection.commit()
  connection.close()

  return {"uuid": uuid}


def list_user_rooms(user: str):
  connection = sqlite3.connect("dispatchx")
  connection.execute(
    "CREATE TABLE IF NOT EXISTS rooms (uuid STRING, usersdump STRING, alias STRING, creator STRING);"
  )
  cursor_object = connection.execute("SELECT * FROM rooms")
  ret = []
  for tup in cursor_object.fetchall():
    print(tup)
    if user in envkeys.decrypt(tup[1],
                               envkeys.string_to_key(envkeys.retrieve(
                                 tup[0]))):
      ret += [{
        "uuid":
        tup[0],
        "members":
        eval(
          envkeys.decrypt(tup[1],
                          envkeys.string_to_key(envkeys.retrieve(tup[0])))),
        "creator":
        envkeys.decrypt(tup[3],
                        envkeys.string_to_key(envkeys.retrieve(tup[0]))),
        "alias":
        envkeys.decrypt(tup[2],
                        envkeys.string_to_key(envkeys.retrieve(tup[0])))
      }]
  connection.commit()
  connection.close()
  return ret
