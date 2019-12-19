def MySort(UnsortedArray,index):
    n=len(UnsortedArray)
    if n==1:
        SortedArray=UnsortedArray
    else:
        midpoint=n//2
        Array1=MySort(UnsortedArray[0:midpoint],index)
        Array2=MySort(UnsortedArray[midpoint:n],index)
        i=0;
        j=0;
        SortedArray=[]
        while i<midpoint and j<n-midpoint:
            if Array1[i][index]<Array2[j][index]:
                SortedArray.append(Array1[i])
                i+=1
            else:
                SortedArray.append(Array2[j])
                j+=1
        if i==midpoint:
            SortedArray+=Array2[j:(n-midpoint)]
        else:
            SortedArray+=Array1[i:midpoint]
    return SortedArray

def distance(P1,P2):
    return ((P1[0]-P2[0])**2+(P1[1]-P2[1])**2)**0.5

def ClosestPair(Array,LeftBound,RightBound):
    # Array is sorted by X
    if RightBound-LeftBound==0: # Array has 1 point
        delta=-1
        Pair=-1
    elif RightBound-LeftBound==1: # Array has 2 points
        delta=distance(Array[LeftBound],Array[RightBound])
        Pair=[Array[LeftBound],Array[RightBound]]
    else: # Array has at least 3 points
        midpoint=(LeftBound+RightBound)//2
        ResultLeft=ClosestPair(Array,LeftBound,midpoint)
        ResultRight=ClosestPair(Array,midpoint+1,RightBound)
        # find delta
        if (ResultRight[1]==-1) or (ResultLeft[1]<ResultRight[1]):
            delta=ResultLeft[1]
            Pair=ResultLeft[0]
        else:
            delta=ResultRight[1]
            Pair=ResultRight[0]
        # find start and stop
        start=0
        while Array[start][0]<Array[midpoint][0]-delta:
            start+=1
        if start>0:
            start-=1
        stop=midpoint+1
        while (stop<RightBound-1) and (Array[stop][0]<Array[midpoint][0]+delta):
            stop+=1
        if stop<RightBound-1:
            stop+=1
        # sort Array[start,stop] based on Y
        n=len(Array)
        temp=[None for i in range(n)]
        for i in range(start,stop+1):
            temp[Array[i][3]]=Array[i]
        i=0
        while i<n:
            if temp[i]==None:
                del(temp[i])
                n-=1
            else:
                i+=1
        # calculate 1:7
        for i in range(len(temp)-1):
            for j in range(i+1,min(i+8,len(temp))):
                d=distance(temp[i],temp[j])
                if d<delta:
                    delta=d
                    Pair=[temp[i],temp[j]]
            
    return [Pair,delta]

X=[95,33,7,87,665,4,2,5,4,8,56,5,13,45,6,87,34,345,1,6,7,67,434,53,24,64]
Y=[23,11,124,27,28,75,28,908,3464,44,167,4,72,48,31,70,47,4,88,36,96,165,8945,36,82,457]
n=len(X)
MyInput=[]
for i in range(n):
    MyInput.append([X[i],Y[i],-1,-1]) # last two are orders in sorted arrays
ArrayYSorted=MySort(MyInput,1)
for i in range(n):
    ArrayYSorted[i][3]=i
ArrayXSorted=MySort(ArrayYSorted,0)
for i in range(n):
    ArrayXSorted[i][2]=i
result=ClosestPair(ArrayXSorted,0,n-1)
print("Coordinates of the points:")
for i in range(n):
    print(ArrayXSorted[i][0],ArrayXSorted[i][1])
print("closest pair:")
print(result[0][0][0],result[0][0][1])
print(result[0][1][0],result[0][1][1])
print("closest distance:")
print(result[1])
