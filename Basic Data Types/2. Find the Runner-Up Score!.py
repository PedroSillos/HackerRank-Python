n = int(input())
arr = list(map(int, input().split()))

n = min(arr)

for x in arr:
    if x > n and x != max(arr):
        n = x
        
print(n)