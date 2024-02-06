tup=(2,4,6,8,9,7,5,3,2,1)
x=2

i=0
while(i<len(tup)):
    if(tup[i]==x):
        print("x is founded at",i)
        break
    else:
        print("x is not present in tup")
        
    i+=1
print("tup is solved")           