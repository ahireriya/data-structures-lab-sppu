def linear(list):
    key=int(input("Enter the Searching Element : "))
    n=len(list)
    flag=0
    for i in range(n):
        if(list[i]==key):
            flag=1
            break
    if(flag==1):
        print("Student is Present")
    else:
        print("Student is not Present")
    
def binary(list):
    key=int(input("Enter the Searching Element : "))
    n=len(list)
  
    low = 0
    high = len(list) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If x is greater, ignore left half
        if list[mid] < key:
            low = mid + 1
 
        # If x is smaller, ignore right half
        elif list[mid] > key:
            high = mid - 1
 
        # means x is present at mid
        else:
            return mid
 
    # If we reach here, then the element was not present
    return -1
result = binary(list)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")

def main():
    list=[]
    n=int(input("Enter the Total Number of Students : "))
    for i in range(n):
        s=int(input("Enter the Roll of Student %d : "%(i+1)))
        list.append(s)
    print("List : ",list)
    print("\n1 : Use Linear Search ")
    print("2 : Use Binary Search")
    ch=int(input("Enter your Choice : "))
    if(ch==1):
        linear(list)
    elif(ch==2):
        binary(list)
    else:
        print("Invalid Choice")
main()
