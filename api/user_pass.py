import sqlite3
import bcrypt
import time, requests
import admins
import secrets
import datetime
from replit import db


def user_exists(username):
  connection = sqlite3.connect("dispatchx")
  res = connection.execute(f"SELECT * FROM users WHERE username='{username}'")
  return len(res.fetchall()) != 0


def contains_profanity(text):
  api_url = f"http://www.purgomalum.com/service/containsprofanity?text={text}"
  response = requests.get(api_url)
  return response.json()


def new_user(username, password):
  connection = sqlite3.connect("dispatchx")
  connection.execute(
    "CREATE TABLE IF NOT EXISTS users(passhash STRING,username STRING, joined INT, UNIQUE(username));"
  )
  if user_exists(username):
    return {
      "message": f"user_{username}_already_exists",
      "code": 409
    }  # 409 conflict
  if contains_profanity(username):
    return {"message": "contains_profanity", "code": 422}
  if len(username) < 3 or username[0].isdigit():
    return {
      "message":
      "username_must_be_longer_than_three_and_start_with_non_number",
      "code": 422
      # 422 unprocessable entity
    }
  connection.execute(
    f"INSERT OR IGNORE INTO users (username, passhash, joined) VALUES (\"{username}\", \"{bcrypt.hashpw(password.encode(),bcrypt.gensalt()).decode()}\", {int(datetime.datetime.utcnow().timestamp())});"
  )
  connection.commit()
  connection.close()
  return {"message": f"success_new_user_{username}"}


def delete_user(username):
  connection = sqlite3.connect("dispatchx")
  connection.execute(f"DELETE FROM users WHERE username='{username}';")
  connection.commit()
  connection.close()
  return {"code": 204, "message": f"user_{username}_deleted"}


def list_users(username):
  if username not in admins.admins:
    return {"code": 403, "message": "you_are_not_an_admin"}
  else:
    connection = sqlite3.connect("dispatchx")
    res = connection.execute(f"SELECT username, joined FROM users;")
    users_info = []
    for user in res.fetchall():
      users_info += {"name": user[0], "joined": user[1]}
  return users_info


def user(username):
  connection = sqlite3.connect("dispatchx")
  res = connection.execute(
    f"SELECT username, joined FROM users WHERE username='{username}';")
  user_info = res.fetchall()
  connection.close()
  if len(user_info) == 0:
    return {"code": 404, "message": "user_not_found"}
  else:
    return {
      "code": 200,
      "message": "success",
      "username": user_info[0][0],
      "joined": user_info[0][1],
      "admin": user_info[0][0] in admins.admins
    }


def matches(username, password):
  connection = sqlite3.connect("dispatchx")
  connection.execute(
    "CREATE TABLE IF NOT EXISTS users(passhash STRING,username STRING, joined INT, UNIQUE(username));"
  )
  res = connection.execute(
    f"SELECT passhash FROM users WHERE username=\"{username}\";")
  try:
    res2 = (res.fetchall()[0][0])
  except IndexError:
    return False
  if bcrypt.checkpw(password.encode(), res2.encode()):
    connection.commit()
    connection.close()
    return True
  else:
    connection.commit()
    connection.close()
    return False
