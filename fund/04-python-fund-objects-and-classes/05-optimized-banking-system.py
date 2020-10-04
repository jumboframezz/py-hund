'''
Optimized Banking System

Create a class BankAccount which has a Name (string), Bank (string) and Balance (decimal).
You will receive several input lines, containing information in the following way:

{bank} | {accountName} | {accountBalance}

You need to store every given Account. When you receive the command “end” you must stop the input sequence.
Then you must print all Accounts, ordered by their balance, in descending order, and then by length of the
bank name, in ascending order.
The accounts must be printed in the following way “{accountName} -> {balance} ({bank})”.
Note: Numbers must be printed rounded to the 2nd decimal digit.

Examples

Input                                   Output
DSK | Ivan | 504.403                    Aleksander -> 20000.00 (DSK)
DSK | Pesho | 2000.4031                 Aleksander -> 20000.00 (Piraeus)
DSK | Aleksander | 20000.0001           Pesho -> 2000.40 (DSK)
Piraeus | Ivan | 504.403                Ivan -> 504.40 (DSK)
Piraeus | Aleksander | 20000.0001       Ivan -> 504.40 (Piraeus)
end

DSK | Ivan | 504.403
DSK | Pesho | 2000.4031
DSK | Aleksander | 20000.0001
Piraeus | Ivan | 504.403
Piraeus | Aleksander | 20000.0001
end
'''


class Account:
    def __init__(self, line):
        in_data = list(line.split(" | "))
        self.bank_name = in_data[0]
        self.acc_holder = in_data[1]
        self.ammount = float(in_data[2])

    def display(self):
        print(f"{self.acc_holder} -> {self.ammount:.2f} ({self.bank_name})")

accounts=[]
in_line = input()
while in_line != "end":
    accounts.append(Account(in_line))
    in_line = input()

sorted_acc = sorted(accounts, key = lambda x: (x.ammount, len(x.bank_name)*-1), reverse=True)
v
for acc in sorted_acc:
    acc.display()