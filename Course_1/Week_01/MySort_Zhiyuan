def MySort(UnsortedArray):
    n=len(UnsortedArray)
    if n==1:
        SortedArray=UnsortedArray
    else:
        midpoint=n//2
        Array1=MySort(UnsortedArray[0:midpoint])
        Array2=MySort(UnsortedArray[midpoint:n])
        i=0;
        j=0;
        SortedArray=[]
        while i<midpoint and j<n-midpoint:
            if Array1[i]<Array2[j]:
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

MyInput=[95,33,7,87,665,4,2,5,4,8,56,5,13,45,6,87,34,345,1,6,7,67,434,53,24,64]
print(MySort(MyInput))
