class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        pers = Person(name, age)
        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            if wife_name in Person.people:
                pers.wife = Person.people[wife_name]
                pers.wife.husband = pers
        person_list.append(pers)
    return person_list
