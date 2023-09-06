# API
### int post(int chatroom, string text)
posts `text` on room id `chatroom`. returns UUID of message
### int del(int chatroom, int uuid)
deletes message with UUID `uuid` from room id `chatroom`. returns success code
### int newroom(string alias, string pass)
creates new room, under name `alias`, password `pass` (none if left empty). returns chatroom id
###  ul listroom(int chatroom)
lists all posts from room id `chatroom`. returns `<ul>` of elements
### int login(string user, string pass)
log in as user `user`, checks password against `pass`. returns success code
### int logout(void)
destroys session, returns success code
### ul userposts(string user, list[int] rooms)
searchs `rooms` for messages from `user`, returns as a `<ul>`

