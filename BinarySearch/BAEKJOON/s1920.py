

n = int(input())
a = sorted(list(map(int,input().split())))
m = int(input())
b = list(map(int,input().split()))

def bi_search(start,end,target):
    while start <= end:
        mid = (start + end) // 2
        if a[mid] == target:
            return True
        elif a[mid] < target:
            start = mid + 1
        else: 
            end = mid -1
    return False

for i in b:
    if bi_search(0,n-1,i) == True:
        print(1)
    else:
        print(0)
