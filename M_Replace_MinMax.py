n = int(input())
arr = []
for i in range(0,n):
    number = int(input())
    arr.append(number)
tmp = arr[arr.index(min(arr))]
print(tmp)
arr[arr.index(min(arr))]= arr[arr.index(max(arr))]
arr[arr.index(max(arr))]=tmp
print(arr)