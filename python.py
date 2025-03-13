from math import *
friend_list = ["Rylie", "Matthew", "Jackson", "Roddy", "David", "Leo"]
object = {"name": "rylie", "age": 19, "gender": "male", "friends": [1, 3, 4]}
friend_list.remove("David")
def friend_maker(friend_name, age, gender, friends) :
    return {"name": friend_name, "age": age, "gender": gender, "friends": friends}
friend = friend_maker("Matthew", 21, "male", [0, 2, 4])
friend_list.sort()
print(object)
print(friend_list)
print(friend)