class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        wife_name = person.get("wife")
        if wife_name:
            Person.people[person["name"]].wife = Person.people[wife_name]

        husband_name = person.get("husband")
        if husband_name:
            Person.people[person["name"]].husband = Person.people[husband_name]

    return persons
