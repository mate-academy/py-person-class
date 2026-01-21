class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for person in people:
        for key in person:
            if key == "wife" and person["wife"] is not None:
                for husband in person_list:
                    if husband.name == person["name"]:
                        for wife in person_list:
                            if wife.name == person["wife"]:
                                husband.wife = wife
            if key == "husband" and person["husband"] is not None:
                for wife in person_list:
                    if wife.name == person["name"]:
                        for husband in person_list:
                            if husband.name == person["husband"]:
                                wife.husband = husband
    return person_list
