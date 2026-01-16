class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []

    for person in people:
        result.append(Person(person["name"], person["age"]))

    for i, person in enumerate(result):
        wife_name = people[i].get("wife")
        husband_name = people[i].get("husband")
        if wife_name:
            person.wife = Person.people[wife_name]
        if husband_name:
            person.husband = Person.people[husband_name]

    return result
