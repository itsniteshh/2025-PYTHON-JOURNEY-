current_users = ["arjun", "ganesh", "aman", "shraddha", "prathmesh", "admin"]

new_users = ["admin", "aman", "Purnima", "pro", "vaibhav", "SHRADDHA"]

for new_user in new_users:
    if new_user in current_users:
        print(f"{new_user} username already exists. Please use a new username")
    else:
        print(f"{new_user} is available for use!")