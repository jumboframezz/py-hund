'''
def read_int_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = map(int, striped_line.split(" "))
    return list(line)


def read_string_line():
    input_line=""
    input_line=input()
    striped_line=input_line.strip()

    line = striped_line.split(" ")
    return list(line)


list_numbers = [-2, -1, -3]
number = list_numbers.pop(list_numbers,-1)
print(number)

phonebook = {}
phonebook["John Smith"] = "+1-555-8976"
phonebook["Lisa Smith"] = "+1-555-1234"
phonebook["Sam Doe"] = "+1-555-5030"
phonebook["Nakov"] = "+359-899-555-592"
phonebook["Nakov"] = "+359-2-981-9819" // Replace
phonebook.pop("John Smith", None)

for key, value in phonebook:
    print("{0} --> {1}".format(key, value))


'''

crit = [",", ":", ";"]
test_text = "alabala,Nica:turska;panica"
print (test_text.split(crit))