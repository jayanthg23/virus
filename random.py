import random
count=0
while(count<=100):
    n=input("press r to roll dice")
    if(n=='r'):
        r=random.randint(1,6)
        count=count+r
        print("your random is",r)
        print("your count is",count)
    if count==8:
        count=37
        print("u have climbed up")
        
