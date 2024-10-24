"""Project 2
Problem Statement:
You want to implement a Binary Search algorithm in Python to efficiently search for a target value in a sorted list.

Question:
How can I write a Python program that uses the Binary Search algorithm to find a target value in a sorted list?"""

def binary_search(arr,target):
  low=0
  high= len(arr)-1

  while low <= high:
    mid =(low + high) //2

    if arr[mid]== target:
      return mid
    elif arr[mid]< target:
      low = mid + 1
    else:
      high=mid -1

  return -1

#take array input from the user
arr = list(map(int,input("Enter space seperated integers:").split()))

#Ask for index value to search
target =int(input("Enter the value to search:"))

#Call binary search function
result =binary_search(arr,target)

#Check for validation
if result != -1:
  print(f"Target value {target} found at index {result}.")
else:
  print(f"Target value{target} not found in the array.")
  