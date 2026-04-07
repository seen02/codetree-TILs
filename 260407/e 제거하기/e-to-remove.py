str = input()

idx = str.index("e")
arr = list(str)
arr.pop(idx)
str = "".join(arr)

print(str)