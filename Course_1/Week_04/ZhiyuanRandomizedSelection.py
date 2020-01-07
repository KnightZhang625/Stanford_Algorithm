import random

def MySwap(MyInput,index1,index2):
    temp = MyInput[index1]
    MyInput[index1] = MyInput[index2]
    MyInput[index2] = temp
    
def partition(MyInput,left,right):
    i = left+1 # first element in the right  
    j = left+1 # last element in the right +1
    while j <= right:
        if MyInput[j] < MyInput[left]:
            MySwap(MyInput,i,j)
            i += 1
        j += 1
    MySwap(MyInput,left,i-1)
    return i-1
    
def rSelection(MyInput,index):
    left = 0
    right = len(MyInput)-1
    random.seed()
    sel = random.randint(left,right)
    MySwap(MyInput,left,sel)
    position = partition(MyInput,left,right)
    while position != index:
        if position > index:
            right = position-1
        else:
            left = position+1
        sel = random.randint(left,right)
        MySwap(MyInput,left,sel)
        position = partition(MyInput,left,right)
    return MyInput[position]
    

if __name__ == "__main__":
    MyInput=[95,33,7,87,665,4,2,5,4,8,56,5,13,45,6,87,34,345,1,6,7,67,434,53,24,64]
    index = 15
    print(rSelection(MyInput,index))