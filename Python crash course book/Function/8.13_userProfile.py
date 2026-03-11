def build_profile (first, last, **user_info):
    """build a dictionary about user_info"""

    user_info["first_name"] = first
    user_info["last_name"] = last

    return user_info

profile = build_profile("Nitesh", "Jha", Location = "Virar", Doing = "Learning")
print(profile)