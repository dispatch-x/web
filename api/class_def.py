import bcrypt, uuid, pickle, sqlite3, codecs

class dispatchxException(Exception):
    pass
class user:
    def __init__(self,username: str,password: str):
        self.username=username
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(8))
        self.password_hash=hashed
        self.uuid=uuid.uuid4()

        connection = sqlite3.connect("dx")
        connection.execute("CREATE TABLE IF NOT EXISTS users (username STRING, pythonuser STRING);")
        
        connection.execute("INSERT INTO users (username, pythonuser) "+f"VALUES ('{self.username}','{codecs.encode(pickle.dumps(self), 'base64').decode()}')")
        connection.commit()
        connection.close()
    def check_hash(self, test_string: str) -> bool:
        if bcrypt.checkpw(test_string.encode('utf-8'), self.password_hash):
            return True
        else:
            return False


def user_from_db(username: str):
  connection = sqlite3.connect("dx")
  connection.execute("CREATE TABLE IF NOT EXISTS users (username STRING, pythonuser STRING);")
  # connection.execute("INSERT INTO My_library (id,author,book) "
  #              "VALUES (1, 'Steve Biko','I write what I like.')")
  cursor_object = connection.execute(f"SELECT * FROM users WHERE username='{username}' ")
  print(cursor_object.fetchall())
  # connection.execute("UPDATE My_library SET book = 'I WRITE WHAT I LIKE' WHERE id = 1")
  # connection.execute("DELETE from My_library WHERE id = 1;")
  connection.commit()
  connection.close()
# def check_user_pass(username: str, password: str) -> bool:
  
#   ouruser=
class message:
    def __init__(self, content: str, username: str, password: str):
        self.content=content

        user_from_db=user_from_db(username)

        # if user_from_db.check_hash(password): no db :)
        #     self.username=username
        # else:
        #     raise dispatchxException("Wrong password ")

o=user("hello","world")
print(o.username,o.password_hash,o.uuid)
print(o.check_hash("world1"), o.check_hash("world"))

user_from_db("hello")