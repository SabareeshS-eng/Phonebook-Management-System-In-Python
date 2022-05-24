a=[]
def partition(a,low,high):
    i=low-1
    p=a[high]
    for j in range(low,high):
        if a[j]<p:
            i+=1
            a[i],a[j]=a[j],a[i]
    a[i+1],a[high]=a[high],a[i+1]
    return i+1
def quicksort(a,low,high):
    if low<high:
        pindex=partition(a,low,high)
        quicksort(a,low,pindex-1)
        quicksort(a,pindex+1,high)
def get(l,n):
    global a
    a = l
    quicksort(a,0,n-1)
    return a