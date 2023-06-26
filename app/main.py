class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({name: self})


def create_person_list(people: list) -> list:

    person_list = []
    for person in people:
        person_list.append(Person(person.get("name"), person.get("age")))
    for i in range(len(people)):
        if people[i].get("wife") is not None:
            person_list[i].wife = Person.people[people[i].get("wife")]
        elif people[i].get("husband") is not None:
            person_list[i].husband = Person.people[people[i].get("husband")]

    return person_list

# people_list = []
#     for person in people:
#         people_list.append(Person(person["name"], person["age"]))
#     for i in range(len(people)):
#             if people[i]["wife"] is not None:
#                 people_list[i].wife = Person.people[people[i]["wife"]]
#             elif people[i]["husband"] is not None:
#                 people_list[i].husband = Person.people[people[i]["husband"]]

#     return people_list
