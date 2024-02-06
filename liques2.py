li1=[1,2,3]
li2=[1,2,3,2,1]

li=li1.copy()
l=li2.copy()

li.reverse()
l.reverse()

if(li == li1):
    print("pallindrome")
else:
    print("not pallindrome")



if(l == li2):
    print("pallindrome")
else:
    print("not pallindrome") 