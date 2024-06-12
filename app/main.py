
class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for single_person in people:
        Person(single_person["name"], single_person["age"])

    for single_person in people:
        person = Person.people[single_person["name"]]

        wife_name = single_person.get("wife")
        if wife_name:
            person.wife = Person.people[wife_name]

        husband_name = single_person.get("husband")
        if husband_name:
            person.husband = Person.people[husband_name]

    return list(Person.people.values())
