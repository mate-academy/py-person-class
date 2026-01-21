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
        person_list.append(pers)
    for person in people:
        pers = Person.people[person["name"]]

        wife_name = person.get("wife")
        if wife_name:
            pers.wife = Person.people[wife_name]

        husband_name = person.get("husband")
        if husband_name:
            pers.husband = Person.people[husband_name]

    return person_list
