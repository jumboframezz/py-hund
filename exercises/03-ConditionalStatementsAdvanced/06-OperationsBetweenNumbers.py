n1 = int(input())
n2 = int(input())
opcode = input()
result = 0
parity = ""
if opcode == "+" or opcode == "-" or opcode == "*":
    if opcode == "+":
        result = n1 + n2
    elif opcode == "-":
        result = n1 - n2
    elif opcode == "*":
        result = n1 * n2
    if result % 2 == 0:
        parity = "even"
    else:
        parity = "odd"
    print(f"{n1} {opcode} {n2} = {result} - {parity}")
elif opcode == "/":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 / n2
        print(f"{n1} / {n2} = {result:.2f}")
elif opcode == "%":
    if n2 == 0:
        print(f"Cannot divide {n1} by zero")
    else:
        result = n1 % n2
        print(f"{n1} % {n2} = {result}")
