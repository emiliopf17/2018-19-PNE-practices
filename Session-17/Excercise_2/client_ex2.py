import json
import termcolor


f = open("person_ex2.json", 'r')


persons = json.load(f)
print("Total people:",len(persons["Persons"]))
people_list = persons["Persons"]
for j, person in enumerate (people_list):

    print()
    termcolor.cprint("Name: ", 'green', end="")
    print(person['Firstname'], person['Lastname'])

    termcolor.cprint("Age: ", 'green', end="")
    print(person['age'])


    phoneNumbers = person['phoneNumber']


    termcolor.cprint("Phone numbers: ", 'green', end='')
    print(len(phoneNumbers))

    # Print all the numbers
    for i, num in enumerate(phoneNumbers):
        termcolor.cprint("  Phone {}:".format(i), 'blue')


        termcolor.cprint("    Type: ", 'red', end='')
        print(num['type'])
        termcolor.cprint("    Number: ", 'red', end='')
        print(num['number'])