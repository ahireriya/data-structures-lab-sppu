array=[]
n=int(input("enter the no of students : "))
def accept():
    for i in range(n):
        num=int(input("enter the marks of the student : "))
        array.append(num)
def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])
    (array[i + 1], array[high]) = (array[high], array[i + 1])
  
    return i + 1

def quick_sort(array, low, high):
    if low < high:

        pi = partition(array, low, high)
        
        quick_sort(array, low, pi - 1)
  
        quick_sort(array, pi + 1, high)
def display():        
    print(f"sorted array {array}")    
def top_score(array):
    print("top five scores")
    count=len(array)
    if (count<5):
        start,stop=count-1,-1
    else:
        start,stop=count-1,count-6
    for i in range(start,stop,-1):
        print (array[i], end=" ")
accept()
quick_sort(array,0,n-1)
display()
top_score(array)