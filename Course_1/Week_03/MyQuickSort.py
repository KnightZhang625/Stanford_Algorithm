import random

def MySwap(MyArray,i,j):
    temp = MyArray[i]
    MyArray[i] = MyArray[j]
    MyArray[j] = temp
  
def MyQuickSort(MyArray,left,right):
    if left == right:
        return
    random.seed()
    pivot = random.randint(left,right)
    MySwap(MyArray,left,pivot)
    i = left+1 # first element in the right  
    j = left+1 # last element in the right +1
    while j <= right:
        if MyArray[j] < MyArray[left]:
            MySwap(MyArray,i,j)
            i += 1
        j += 1
    MySwap(MyArray,left,i-1)
    if i > left+2:
        MyQuickSort(MyArray,left,i-2)
    if right > i:
        MyQuickSort(MyArray,i,right)

MyInput=[95,33,7,87,665,4,2,5,4,8,56,5,13,45,6,87,34,345,1,6,7,67,434,53,24,64]
print('original:')
print(MyInput)
MyQuickSort(MyInput,0,len(MyInput)-1)
print('after quick sort:')
print(MyInput)
