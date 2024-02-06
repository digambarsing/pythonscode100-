# it is all about lists
# it is builtin dtattype to store different datatype.
# it is mutable


student=['ved',24,'GLA',3000]
print(student)
print(type(student))


# slicing

print(student[1:4])
print(student[1:])
print(student[:4])
print(student[-4:-1])


# list methods



li=[34,2,56,4,87,45]

li.append(4)
print(li)




li.sort()
print(li)

li.sort(reverse=True)
print(li)

li.reverse()
print(li)


li.insert(0,78)
print(li)

li.remove(56)
print(li)

li.pop(0)
print(li)
