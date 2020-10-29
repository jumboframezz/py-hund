
# _ in loops
for _ in range (3):
    print (f"Outside: {_}")
    for _ in range(3):
        print(f"Inside  {_}")
    print("--------")

# Another use of _ to initialise an array
m = [f"value {_}" for _ in range(10)]
print(m)
