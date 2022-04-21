t = int(input())
for test in range(t):
    data = list(map(int,input().split()))
    tot = 0
    for i in data:
        if i%2 == 1:
            tot += i
    print('#'+str(test),tot)
