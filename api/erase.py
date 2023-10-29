from replit import db
import os, time

print(
  "This is a destructive process. Please review whether this should be ran. (wait)"
)
time.sleep(5)
if input("If you are sure, type 'Yes, do as I say' with all punctuation: "
         ) == "Yes, do as I say":
  for item in db.keys():
    del db[item]
  try:
    os.remove("dispatchx")
  except FileNotFoundError:
    pass
  try:
    os.remove("dx")
  except FileNotFoundError:
    pass
  print("Database has been deleted")
else:
  print("Aborted")