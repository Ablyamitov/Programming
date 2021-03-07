_print = print
def create(n,x0,d):
    arr.append(x0)
    for i in range(1,n):
        arr.append(arr[i-1]+d)
    return arr

def sort(arr,n):
    for i in range (n-1):
        key = i+1
        temp = arr[key]
        for j in range(i+1,-1,-1):
            if (temp<arr[j-1]):
                arr.append(arr[j-1])
                key = j-1
        arr[key]=temp
    return arr

def print(arr,n):
    _print('[', end=" ")
    for i in range (n):
        if(i<n-1):
            _print(arr[i], end = ", ")
        else:
            _print(arr[i],"]")



n = int(input())
x0 = int(input())
d = int(input())
arr=[]

arr = create(n,x0,d)
arr = sort(arr,n)
arr = print(arr,n)