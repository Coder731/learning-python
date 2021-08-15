users = ['anna','chris','brian']
for user in range(len(users)):

    a=users[user]
    print("a="+a)

    b=users[user].capitalize()
    print("b="+b)

    c=str(user)
    print("c="+c)

    users[user]=b



print(users)