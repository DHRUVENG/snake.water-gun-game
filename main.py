'''
1 for sanke
-1 for water
0 for gun
'''
import random
computer=random.choice([1,-1,0])

youstr=(input("enter the string: "))
youdic={
    "snake":1,
    "water":-1,
    "gun": 0
    
}
reversedic={
    1:"snake",
    -1:"water",
    0:"gun"
}
you=youdic[youstr]
print(f"you chose {reversedic[you]}\ncomputer chosse {reversedic[computer]}")
if(computer==you):
    print("it draw")
else:    
    if(computer==-1 and you==1):
        print("you win")
    elif(computer==-1 and you==0):
        print("you lose")    
    elif(computer==1 and you==-1):
        print("you win")    
    elif(computer==1 and you==0):
        print("you win")    
    elif(computer==0 and you==-1):
        print("you win") 
    elif(computer==0 and you==1):
        print("you lose")  
    else:
        ("some thing went wrong")    


