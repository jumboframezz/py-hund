

arr = [f"element {_}" for _ in range(10)]


print(f"arr: {arr}")
print(f"len: {len(arr)}")

for i in range(len(arr) - 1, -1, -1 ):
    print(arr[i])