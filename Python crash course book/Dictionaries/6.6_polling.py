fav_lang = {
    "nitesh": "python",
    "aman": "excel", 
    "pro": "bi",
    "vaibhav": "tableau"
}

friends = ["aman", "purnima", "arjun", "ganesh", "pro"]
new_frnds = []

for k in fav_lang.keys():
    new_frnds.append(k)

for f in friends:
    if f in new_frnds:
        print(f"Thanks for being my friend {f}")
    else:
        print(f"Welcome my new friend, {f}")