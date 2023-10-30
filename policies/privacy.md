## Dispatchx Privacy Policy
This piece of software is licensed under the Mozilla Public License 2.0, a version of which is kept in `../LICENSE`.
### 1 - User Data
We do not store any identifying details of users that are not provided to us. We also do not access any user details, or glean any data from the `messages` table.
#### Table Structure - `users`
Nothing in this table is encrypted, but the password is hashed. No encryption is needed as the other 3 columns are public knowledge through the `api/v2/user/<user>` api.
| password hash | username | joined date | status |
| - | - | - | - |
### 2 - Chatroom Data
Each chatroom has its own row in `rooms`, containing the room uuid, used so that multiple rooms can have the same alias, the alias (nickname) of a room (encrypted), the list of users in the room (encrypted), and the creator of the room (encrypted).
#### Table Structure - `rooms`
| room uuid | users | alias | creator |
| - | - | - | - |
### 3 - Message Data
Messages are stored with a room uuid in the `messages` table. The data stored contains the message uuid, the room uuid, the sender (encrypted), the content (encrypted), and the UTC timestamp of when it was sent. Messages have a uuid, but the are not currently in use, rather there for future purposes such as message deletion.
#### Table Structure - `messages`
| room uuid | message uuid | content | sender | sent time |
| - | - | - | - | - |