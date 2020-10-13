# 3.	Клас животно
# Напишете програма, която отпечатва класа на животното според неговото име, въведено от потребителя.
# 1. dog -> mammal
# 2. crocodile, tortoise, snake -> reptile
# 3. others -> unknown


animal = input()

if animal == "dog":
    print("mammal")
elif animal == "crocodile" or animal == "tortoise" or animal == "snake":
    print("reptile")
else:
    print("unknown")
