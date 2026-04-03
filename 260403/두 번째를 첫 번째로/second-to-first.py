str = input()

arr = list(str)
c = arr[1]

for i in range(len(arr)):
    if arr[i] == c:
        arr[i] = arr[0]

str = ''.join(arr)

print(str)