'''
Blank Receipt

Create a function that prints a blank cash receipt. The function should invoke three other functions: one for printing
the header, one for the body and one for the footer of the receipt.
The header should contain the following text:

CASH RECEIPT
------------------------------

The body should contain the following text:

Charged to____________________
Received by___________________

And the text for the footer:

------------------------------
© SoftUni

'''


def print_header():
    print("CASH RECEIPT")
    print("------------------------------")


def print_body():
    print("Charged to____________________\nReceived by___________________")


def print_footer():
    print("------------------------------\n© SoftUni")


def print_receipt():
    print_header()
    print_body()
    print_footer()

print_receipt()
