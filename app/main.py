


class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people_list: list) -> list:
    out_list = []
    for man in people_list:
        new_person = Person(man["name"], man["age"])
        if man.get("husband"):
            new_person.husband = man["husband"]
        elif man.get("wife"):
            new_person.wife = man["wife"]

        out_list.append(new_person)

    for  name, man in Person.people.items():
        print(name, "   ", man)
        if "wife" in man.__dict__:
            man.wife = Person.people[man.wife]
        elif "husband" in man.__dict__:
            man.husband = Person.people[man.husband]

    return out_list
#
# people = [
#         {"name": "Ross", "age": 30, "wife": "Rachel"},
#         {"name": "Joey", "age": 29, "wife": None},
#         {"name": "Rachel", "age": 28, "husband": "Ross"}
#     ]
#
#
# person_list = create_person_list(people)
# print(person_list)
# print(isinstance(person_list[0], Person))
# print(person_list[0].name)
#
# print(person_list[0].name == "Ross")
# print(person_list[0].wife is person_list[2]) # True
# print(person_list[0].wife.name == "Rachel")
#
# print(person_list[1].name == "Joey")
# #person_list[1].wife
# # AttributeError
#
# print(isinstance(person_list[2], Person)) # True
# print(person_list[2].name == "Rachel")
# print(person_list[2].husband is person_list[0]) # True
# # The same as person_list[0]
# print(person_list[2].husband.name == "Ross")
# print(person_list[2].husband.wife is person_list[2])  # True
#
# print(person_list)
# print(Person.people)
#
