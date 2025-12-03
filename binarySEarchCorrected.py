arr=[]
n=int(input("ENter the numbber of element:"))
for i in range(n):
    value=int(input(f"Element {i+1}:"))
    arr.append(value)
arr.sort()
print("The sorted array:",arr)
choice=int(input("Enter your choice:"))
left=0
right=len(arr)-1
position=-1
while left<=right:
    middle=(left+right)//2
    if choice==arr[middle]:
        position=middle
        break
    elif choice>arr[middle]:
        left=middle+1
    else:
        right=middle-1
if position==-1:
    print("Not found")
else:
    print(f"Targeted value {choice} is found at {position+1} position")


