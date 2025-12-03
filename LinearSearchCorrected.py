arr=[3,5,8,7,17,6,9]
choice=int(input("Enter the value you want:"))
position=-1 # initially say no position
for i in range(len(arr)):
    if choice==arr[i]:
        position=i
        break
if position==-1: # out of the array
        print("Target value not found")
else:
        print(f"Targeted value is {choice}  at {position+1}  position") #pos+1 because array starts from 0





