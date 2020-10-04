'''
Animals *

You have been given the task to create classes for several sophisticated animals.

Create a class Dog which has a name (string), age (int) and number_of_legs (int).
Create a class Cat which has a name (string), age (int) and intelligence_quotient (int).
Create a class Snake which has a name (string), age(int) and cruelty_coefficient (int).

Create a method in each class which is called produce_sound(). The method should print on the console a string depending on the class:

If it’s a Dog, you should print “I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.”
It it’s a Cat, you should print “I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.”
If it’s a Snake, you should print “I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.”

Now for the real deal. You will receive several input commands, which will register animals or make them produce sounds, until you receive
the command “I’m your Huckleberry”.

The commands will be in the following format:
{class} {name} {age} {parameter}
The class will be either “Dog”, “Cat” or “Snake”. The name will be a simple string, which can contain any ASCII character BUT space. The age will be an integer.
The parameter, will be an integer. Depending on the class it would either be number of legs, IQ, or cruelty coefficient.

Register each animal, and keep them in collections, by your choice, so that you can ACCESS THEM BY NAME. You will most likely need 3 collections,
to store the different animals inside them.

Between the register commands you might receive a command in the following format:

talk {name}
You must then make the animal with the given name, produce a sound.

When you receive the ending command, you should print every animal in the following format:
If it’s a Dog, you should print “Dog: {name}, Age: {age}, Number Of Legs: {numberOfLegs}”
It it’s a Cat, you should print “Cat: {name}, Age: {age}, IQ: {intelligenceQuotient}”
If it’s a Snake, you should print “Snake: {name}, Age: {age}, Cruelty: {crueltyCoefficient}”
Print first the Dogs, then the Cats, and lastly – The Snakes.

Constraints
You can assume that there will be no duplicate names (even in different animals).
All input data will be valid. There will be no invalid input lines.
The name in the talk command, will always be existent.

Examples
Input                           Output
Dog Sharo 3 4                   I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.
Cat Garfield 5 200              I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.
Snake Alex 25 1000              I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.
talk Sharo
talk Garfield
talk Alex
I'm your Huckleberry            Dog: Sharo, Age: 3, Number Of Legs: 4
                                Cat: Garfield, Age: 5, IQ: 200
                                Snake: Alex, Age: 25, Cruelty: 1000

Dog Sharo 3 4
Cat Garfield 5 200
Snake Alex 25 1000
talk Sharo
talk Garfield
talk Alex
I'm your Huckleberry

'''


class Dog:
    def __init__(self, age, legs):
        self.age = age
        self.legs = legs

    def produce_sound(self):
        print("I'm a Distinguishedog, and I will now produce a distinguished sound! Bau Bau.")
    def display(self, name):
        print(f"Dog: {name}, Age: {self.age}, Number Of Legs: {self.legs}")

class Cat:
    def __init__(self, age, iq):
        self.age = age
        self.iq = iq

    def produce_sound(self):
        print("I'm an Aristocat, and I will now produce an aristocratic sound! Myau Myau.")
    def display(self, name):
        print(f"Cat: {name}, Age: {self.age}, IQ: {self.iq}")

class Snake:
    def __init__(self, age, cruelty):
        self.age = age
        self.cruelty = cruelty
    def produce_sound(self):
        print("I'm a Sophistisnake, and I will now produce a sophisticated sound! Honey, I'm home.")
    def display(self, name):
        print(f"Snake: {name}, Age: {self.age}, Cruelty: {self.cruelty}")

in_line = input()
dogs = {}
cats = {}
snakes = {}
while in_line != "I'm your Huckleberry":
    line = in_line.split(" ")
    name = line[1]
    if line[0] == "Dog":
        dogs[name] = Dog(line[2], line[3])
    elif line[0] == "Cat":
        cats[name] = Cat(line[2], line[3])
    elif line[0] == "Snake":
        snakes[name] = Snake(line[2], line[3])
    elif line[0] == "talk":
        if name in dogs:
            dogs[name].produce_sound()
        elif name in cats:
            cats[name].produce_sound()
        elif name in snakes:
            snakes[name].produce_sound()
    in_line = input()




for i in dogs:
        dogs[i].display(i)
for i in cats:
        cats[i].display(i)
for i in snakes:
        snakes[i].display(i)

























