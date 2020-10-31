

# arr = [f"element {_}" for _ in range(10)]
#
#
# print(f"arr: {arr}")
# print(f"len: {len(arr)}")
#
# for i in range(len(arr) - 1, -1, -1 ):
#     print(arr[i])
#



arr = [1, 2, 3, 4, 5 ,6]
for _ in range(len(arr)):
    print(f"index: {_} : {arr[_]} {len(arr)}")
    arr.remove(arr[_])