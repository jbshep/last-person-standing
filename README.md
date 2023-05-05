# last-person-standing

This project creates a Dockerfile that creates an image for Dr. Shepherd's "Last Person Standing" contest in DevOps.  However, it can be used any time to spin up a Linux Docker instance with pre-created users and sshd running.

To define users that will be created, create a file named `users.py` and have that code generate a list named `users`.  Otherwise, usernames can be entered from the command line.

## Usage

```
# First, create users list in users.py
# Then, ...
python3 create-dockerfile.py
docker build -t lpstand .
docker run -dp <port>:22 lpstand
```

## Connecting

```
ssh -l <user> -p <port> localhost
sftp -P <port> <user>@localhost
```
