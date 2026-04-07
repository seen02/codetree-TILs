str = input()

arr = list(str)
arr.pop(-2)
arr.pop(2)

str = "".join(arr)
print(str)