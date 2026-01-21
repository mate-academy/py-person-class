class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        pers = Person(person["name"], person["age"])

        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            if wife_name in Person.people:
                pers.wife = Person.people[wife_name]
                pers.wife.husband = pers

        if "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            if husband_name in Person.people:
                pers.husband = Person.people[husband_name]
                pers.husband.wife = pers

        person_list.append(pers)

    return person_list
