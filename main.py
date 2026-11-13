# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/



"""---------------------------"""
people = [
    {"name": "Ross", "age": 30, "wife": "Rachel"},
    {"name": "Joey", "age": 29, "wife": None},
    {"name": "Rachel", "age": 28, "husband": "Ross"}
]

person_list = create_person_list(people)
isinstance(person_list[0], Person) # True
person_list[0].name == "Ross"
person_list[0].wife is person_list[2] # True
person_list[0].wife.name == "Rachel"

person_list[1].name == "Joey"
person_list[1].wife
# AttributeError

isinstance(person_list[2], Person) # True
person_list[2].name == "Rachel"
person_list[2].husband is person_list[0] # True
# The same as person_list[0]
person_list[2].husband.name == "Ross"
person_list[2].husband.wife is person_list[2]  # True

Person.people == {
    "Ross": <__main__.Person object at 0x10c20ca60>,
    "Joey": <__main__.Person object at 0x10c180a00>,
    "Rachel": <__main__.Person object at 0x10c1804f0>
}