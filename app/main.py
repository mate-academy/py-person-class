class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(income_people_list: list) -> list:
    created_person_list = []

    for person_dict in income_people_list:
        person = Person(person_dict["name"], person_dict["age"])
        created_person_list.append(person)

    for i in range(len(income_people_list)):
        if "wife" in income_people_list[i] and\
                income_people_list[i]["wife"] is not None:
            created_person_list[i].wife = Person.people[
                income_people_list[i]["wife"]
            ]
        if "husband" in income_people_list[i] and\
                income_people_list[i]["husband"] is not None:
            created_person_list[i].husband = Person.people[
                income_people_list[i]["husband"]
            ]

    return created_person_list
