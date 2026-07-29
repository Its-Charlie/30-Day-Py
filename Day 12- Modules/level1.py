#Random User ID:
import random
import string

def random_user_id():
    characters = string.ascii_letters + string.digits
    user_id = ""

    for i in range(6):
        user_id += random.choice(characters)

    return user_id

print(random_user_id())

#User ID Generator
import random
import string

def user_id_gen_by_user():
    length = int(input("Enter number of characters: "))
    count = int(input("Enter number of IDs: "))

    characters = string.ascii_letters + string.digits

    for i in range(count):
        user_id = ""
        for j in range(length):
            user_id += random.choice(characters)
        print(user_id)

user_id_gen_by_user()