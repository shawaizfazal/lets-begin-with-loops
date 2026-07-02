string=input("please enter your name")
char=input("please enter your character")
i=0
count=0
while(i<len(string)):
    if(string[i]==char):
     count=count+1
    i=i+1
print("the total number of time" , char," has occured=", count)
