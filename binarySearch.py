def binarySearch (arr, l, h, x):
  if h >= l:

     mid = l + (h- l)//2
     if arr[mid] == x:
       return mid

     elif arr[mid] > x:
       return binarySearch(arr, l, mid-1, x)

     else:
       return binarySearch(arr, mid+1, h, x)

  else:
     return -1

n = int(input("Enter number of elements of array: "))
arr=[]
for i in range(0,n):
    element_arr = int(input(f"The {i+1}st element in array is: "))
    arr.append(element_arr)
print(arr)



number=input("Enter the number i.e. x :")
x=int(number)
search=binarySearch(arr ,0 ,len(arr) - 1 ,x )
if search != -1:
   print (f"{x} is present at index "+str(search))
else:
   print (f"{x} is not present in array")
