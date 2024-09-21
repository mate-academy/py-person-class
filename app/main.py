class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            (Person.people[person.get("name")].__dict__
             .update({"wife": Person.people[person.get("wife")]}))

        if person.get("husband"):
            (Person.people[person.get("name")].__dict__
             .update({"husband": Person.people[person.get("husband")]}))

    return person_list


# people = [
#     {"name": "Ross", "age": 30, "wife": "Rachel"},
#     {"name": "Joey", "age": 29, "wife": None},
#     {"name": "Rachel", "age": 28, "husband": "Ross"}
# ]
#
# person_list = create_person_list(people)
# # print(person_list)
# # print(person_list[0].__dict__)
#
# print("-"*30)
# print("Person.people: ", Person.people)
# print("-"*30)
# for person in Person.people.values():
#     print(person.__dict__)
# print("-"*30)

# ------------------------------------------------------------
# print("-"*39)
# print(isinstance(person_list[0], Person))
# print(person_list[0].name == "Ross")
# print(person_list[0].wife is person_list[2])
# print(person_list[0].wife.name == "Rachel")
# print(person_list[1].name == "Joey")
# print(person_list[1].wife)
# print(person_list[1].name == "Joey")
# print(person_list[2].name == "Rachel")
# print(person_list[2].husband is person_list[0])
# print(person_list[2].husband.name == "Ross")
# print(person_list[2].husband.wife is person_list[2])
# print(Person.people)
# ------------------------------------------------------------
# print("-"*39)

# some_person = Person("Ross", 30)
# print(some_person.person)
# Person.person.update({some_person.name: some_person})

# print(Person.__dict__)
# print(some_person.__class__.__dict__)
