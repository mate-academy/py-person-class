class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    les = []

    for obj in people:
        les.append(Person(obj["name"], obj["age"]))

    for obj in people:
        if "husband" in obj:
            if isinstance(obj["husband"], str):
                Person.people[obj["name"]].husband\
                    = Person.people[obj["husband"]]

    for obj in people:
        if "wife" in obj:
            if isinstance(obj["wife"], str):
                Person.people[obj["name"]].wife = Person.people[obj["wife"]]

    return les


# people = [
#     {'name': 'Ross', 'age': 30, 'wife': 'Rachel'},
#     {'name': 'Joey', 'age': 29, 'wife': None},
#     {'name': 'Rachel', 'age': 28, 'husband': 'Ross'}
# ]

# person_list = create_person_list(people)
# print(person_list)
# # print(isinstance(person_list[0], Person))  # True
# # print(person_list[0].name)
# # print(person_list[0].wife is person_list[2])  # True
# # print(person_list[0].wife.name)  # 'Rachel'
# # #
# # print(person_list[1].name)  # == 'Joey'
# print(person_list[1].wife)
# AttributeError
#
# isinstance(person_list[2], Person) # True
# person_list[2].name == 'Rachel'
# person_list[2].husband is person_list[0] # True
# # The same as person_list[0]
# person_list[2].husband.name == 'Ross'
# person_list[2].husband.wife is person_list[2]  # True

# Person.people == {
#     'Ross': <__main__.Person object at 0x10c20ca60>,
#     'Joey': <__main__.Person object at 0x10c180a00>,
#     'Rachel': <__main__.Person object at 0x10c1804f0>
# }
