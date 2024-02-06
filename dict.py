# info={
#     "name":"ved",
#     "age":45,
#     "study":['python','web'],
#     "friends":('ved','dev'),
#     "student":{
#         "roll":45,
#         "interest":"games"
#     }
# }

# print(info)


# # access data

# print(info["name"])


# print(info["student"]["roll"])



stud={
    "name":"ved",
    "age":45

}

stud["name"]="dev"
print(stud)


print(stud.keys())
print(stud.values())
print(stud.items())
print(stud.get("name"))
# print(stud.update("name":"radhe"))