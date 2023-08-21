class Person:
    people = {}

    def __init__(self, name: object, age: object) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persone_list = []
    for person in people:
        persone_list.append(Person(name=person["name"], age=person["age"]))

    for persone in people:
        for pers in persone_list:
            if persone.get("name") == pers.name and persone.get("wife") is not None:
                for wife_name in persone_list:
                    if wife_name.name == persone.get("wife"):
                        pers.wife = wife_name
            if persone.get("name") == pers.name and persone.get("husband") is not None:
                for husband_name in persone_list:
                    if husband_name.name == persone.get("husband"):
                        pers.husband = husband_name
    return persone_list
