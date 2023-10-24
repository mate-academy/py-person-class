class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.setdefault(name, self)


def create_person_list(people: list) -> list:
    person_list = []

    for people_dict in people:
        person = Person(people_dict["name"], people_dict["age"])
        print(person.__dict__)
        person_list.append(person)

    for ind, spouses in enumerate(people):
        if "wife" in spouses and spouses["wife"] is not None:
            # print(spouses)
            # print("spouses[wife]:\t", spouses["wife"])
            # print("Person.people.get:\t", Person.people.get(spouses["wife"]).name)
            wife = Person.people.get(spouses["wife"])
            person_list[ind].wife = wife
            wife.husband = person_list[ind]
        if "husband" in spouses and spouses["husband"] is not None:
            # print(spouses)
            # print("spouses[husband]:\t", spouses["husband"])
            # print("Person.people.get:\t", Person.people.get(spouses["husband"]).name)
            husband = Person.people.get(spouses["husband"])
            person_list[ind].husband = Person.people.get(spouses["husband"])
            husband.wife = person_list[ind]
    print(person_list)
    return person_list

# if __name__ == "__main__":
#     person_test = [
#         {"name": "Ross", "age": 30, "wife": "Rachel"},
#         {"name": "Joey", "age": 29, "wife": None},
#         {"name": "Phoebe", "age": 31, "husband": None},
#         {"name": "Chandler", "age": 30, "wife": "Monica"},
#         {"name": "Monica", "age": 32, "husband": "Chandler"},
#         {"name": "Rachel", "age": 28, "husband": "Ross"},
#     ]
#
#     person_list = create_person_list(person_test)
#     print(Person.people)
#     for person in person_list:
#         print(person.__dict__)



