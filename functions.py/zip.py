usernames = ["Dude","Bro","Mister"]
passwords = ("p@ssword","abc123","guest")
login_date = ["1/1/2022","1/2/2022","1/3/2022"]

users = dict(zip(usernames,passwords))

for key, value in users.items():
    print(key + ": "+ value)


users = zip(usernames,passwords,login_date)

for i in users:
    print(i)
