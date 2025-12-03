num=[]
n=int(input("Enter the numbers of element:"))
for i in range(n):
    value=int(input(f"numbers {i+1}:"))
    num.append(value)
print("The unsorted array is:",num)
def sorting(num):
    for i in range(len(num)-1,0,-1):
        for j in range(i):
            print(f"All the passess in array {j+1}")
            if num[j]>num[j+1]:
                temp=num[j]
                num[j]=num[j+1]
                num[j+1]=temp
sorting(num)
print("The sorted array is:",num)
