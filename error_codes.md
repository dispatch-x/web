## Error codes
HTTP-style error codes. This does not detail any other that may occur, for example 500 for a bad line of PHP.

```json
{
    "400": {
        "description": "Bad request",
        "routes": [
            {
                "name": "del",
                "reason": "uuid not found" 
            },
            
        ]
    },
    "401": {
        "description": "User needs to be logged in to perform this action.",
        "routes": [
            {
                "name": "post",
                "reason": "user is not authorized to post on this chatroom" 
            },
            {
                "name": "del",
                "reason": "user is not authorized to delete this message" 
            },
            {
                "name": "listroom",
                "reason": "user is not authorized to access this chatroom" 
            },
            {
                "name": "listuser",
                "reason": "user is not authorized to access one of these chatrooms" 
            },
            {
                "name": "login",
                "reason": "user's password is incorrect"
            }
        ]
    },
    "404": {
        "description": "Rescource not found on this server",
        "routes": [
            {
                "name": "login",
                "reason": "user not found" 
            },
            {
                "name": [
                    "post",
                    "del",
                    "listroom",
                    "listuser"
                ],
                "reason": "one or all of the provided rooms do not exist" 
            },
            
        ]
    },
}
```

### Example
- user tries to post without being logged in
response:
```json
{
    "code": "401",
    "message:": "user needs to be logged in to perform this action.",
    "reason": "user is not authorized to post on this chatroom"
}
```
