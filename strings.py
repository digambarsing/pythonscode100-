name="ved"
Name='dev'
namE='''vidhya'''

print(name)
print(Name)
print(namE)



# concatente method


print(name+" "+ namE)


# length function

print(len(name))
print(len(namE))


# indexing

print(name[0])
print(name[1])

# slicing

print(name[0:2])  # last index is not involved.
print(name[0:])
print(name[:2])

# negative slicing
print(name[-2:])


# endswith function

print(name.endswith('ed'))
print(name.endswith('e'))
print(name.endswith('d'))

# count function

print(name.count('e'))
print(name.count('d'))


# find function

print(name.find('ved'))
print(name.find("ted"))




# capitalize function

print(name.capitalize())
print(namE.capitalize())


# replace function

print(name.replace('v','t'))

