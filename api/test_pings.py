import requests
import json


def ping(route, params):
  url = f'https://api.dispatch.eu.org/api/v2/{route}'
  response = requests.get(url, params)
  return response.json()


user = input("Please enter a username ")
pw = input("Please enter a password ")
msg = input("Please enter a message ")

usero = input("Please enter a username for another, pre registered account ")
passo = input("Please enter the password for said account ")

print(f"""
Should return new user created (unless user already exists)
{ping(
  f'/users/new', {"user": user, "password": pw}
)}

Should return 409 already exists
{ping(
  f'/users/new', {"user": user, "password": pw}
)}
""")
r_uuid = ping(
  '/rooms/create', {
    "user": user,
    "password": pw,
    "alias": f"{user}room",
    "users": f"{user},test1,test2"
  })
ping('/rooms/create', {
  "user": user,
  "password": pw,
  "alias": f"{user}room2",
  "users": f"{user}"
})
if "uuid" not in r_uuid:
  print(r_uuid)
  exit(-1)
print(f"""
Should return success new room
{r_uuid}

Should return successful post
{ping(
  f'/rooms/{r_uuid["uuid"]}/post', {"user": user, "password": pw,  "msg": msg}
)}

Should return a list with previous post
{ping(
  f'/rooms/{r_uuid["uuid"]}/messages', {"user": user, "password": pw})
}

Should return error, user not in room

{ping(
  f'/rooms/{r_uuid["uuid"]}/messages', {"user": usero, "password": passo})
}

Should return list of all rooms user is in
{ping(f'/user/{user}/rooms', {'password': pw})}
""")
# /user/<user>/delete is in pre-alpha testing, don't add yet, user not purged from rooms etc.
