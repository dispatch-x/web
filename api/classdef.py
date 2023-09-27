import bcrypt, uuid

class dispatchxException(Exception):
    pass
class user:
    def __init__(self,username: str,password: str):
        self.username=username
        hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt(8))
        self.password_hash=hashed
        self.uuid=uuid.uuid4()
    def check_hash(self, test_string: str) -> bool:
        if bcrypt.checkpw(test_string.encode('utf-8'), self.password_hash):
            return True
        else:
            return False

class message:
    def __init__(self, content: str, username: str, password: str):
        self.content=content

        user_from_db=NotImplemented

        # if user_from_db.check_hash(password): no db :)
        #     self.username=username
        # else:
        #     raise dispatchxException("Wrong password ")

# o=user("hello","world")
# print(o.username,o.password_hash,o.uuid)
# print(o.check_hash("world1"), o.check_hash("world"))