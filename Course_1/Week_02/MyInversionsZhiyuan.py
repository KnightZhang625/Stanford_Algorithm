def ReadFile(file_path):
    data=[]
    f = open(file_path, 'r')
    for c in f.readlines():
        c_array=c.split('\n')
        data.append(int(c_array[0]))
    return data    

def MySort(UnsortedArray):
    n=len(UnsortedArray)
    if n==1:
        Inversions=0
        SortedArray=UnsortedArray
    else:
        midpoint=n//2
        [Inversions1,Array1]=MySort(UnsortedArray[0:midpoint])
        [Inversions2,Array2]=MySort(UnsortedArray[midpoint:n])
        i=0;
        j=0;
        Inversions=Inversions1+Inversions2
        SortedArray=[]
        while i<midpoint and j<n-midpoint:
            if Array1[i]<Array2[j]:
                SortedArray.append(Array1[i])
                i+=1
            else:
                SortedArray.append(Array2[j])
                j+=1
                Inversions+=midpoint-i
        if i==midpoint:
            SortedArray+=Array2[j:(n-midpoint)]
        else:
            SortedArray+=Array1[i:midpoint]
    return [Inversions, SortedArray]

MyInput=ReadFile("data.txt")
print(MySort(MyInput)[0])


