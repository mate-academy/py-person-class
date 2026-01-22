class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    for person in people:
        name = person["name"]
        age = person["age"]
        persons.append(Person(name, age))

    for person in people:
        name = person["name"]
        spouse_name = person.get("wife") or person.get("husband")
        if spouse_name:
            if "wife" in person:
                Person.people[name].wife = Person.people[spouse_name]
            elif "husband" in person:
                Person.people[name].husband = Person.people[spouse_name]
    return persons
