import random
list=["LAGAAN","ANAND","3IDIOTS","DANGAL","SWADES","AWEDNESDAY","UDAAN","SPECIAL26","SULTAN","HAIDER","QUEEN","BARFI","GURU",
"SARKAR","DRISHYAM","BABY","PK","AIRLIFT","HOLIDAY","GOODNEWWZ","KAHANI","BLACK","GOLMAAL","CHUPKECHUPKE","SHOLAY","DEEWAR",
"KESHARI","SHAHENSHAH","SHARABI","COOLIE","WAZIR","MANJHI","DON","ANDHADUN","PINK","LOOTERA","BADLA","AGNEEPATH","HUM","NEERJA",
"THELUNCHBOX","VEERZARA","MSDHONI","MANN","DIL","DHADKAN","ISHQ","KHILADI","ANARI","BADSHAH","BAZIGAR"]

movie=random.choice(list)

n=(len(movie))
f=0
k=0
arr=[]
for i in range(0,n):
    arr.append("_")
    
print("You have got 7 trials to enter the movie name .")
print("If u can't guess the name, then you can simply enter a letter.")
print()
for i in range(0,n):
                print(arr[i]," ",end=" ")
tr=1
while(tr<=7):
    print("Guess the movie if u can else enter a letter!")
    inp=input().upper()
    print()
    if(len(inp)==n or arr==movie):
        if(inp == movie):
            print("Hurray! You won. Yes the answer was",movie)
            f=1
            break
        else:
            print("Sorry,thats not right.")
            print("You still have",7-tr," turns left.Try again.")
            print()
            for i in range(0,n):
                print(arr[i]," ",end="")
            print()
            inp=input().upper()
            tr=tr+1
            continue
    elif(len(inp)==1):
        for i in range(0,n):
            c=movie[i]
            if(inp==c):
                arr[i]=c
                k=1
        for i in range(0,n):
                print(arr[i]," ",end="")
        print()
        if(k==1):
            print("Yes ",inp," letter is presnt in this movie name.")
            print("You still have",7-tr," turns left.",end=" ")
        else:
            print("Sorry",inp," is not there.")
            print("You still have",7-tr," turns left. Try again.")
        k=0
        tr=tr+1
        continue
        
    print("Sorry,thats not right. Try again.")
    print("You still have",7-tr," turns left.Try again.")
    print()
    inp=input()
    tr=tr+1
    

print()
if f!=1:
    print("Sorry,the answer was",movie)
    
