users = [
    {"name": "Alice", "role": "admin"},
    {"name": "Bob", "role": "user"},
    {"name": "Charlie", "role": "admin"},
    {"name": "David"},
    {"name": "Eve", "role": "moderator"}
]
#Print only the users who have the role "admin" via a loop
for user in users:
    try:
        if user["role"] == "admin":
            print(user["name"])
    except KeyError:
        continue