class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        target_person = Person.people[person.get("name")]

        if wife_name := person.get("wife"):
            target_person.wife = Person.people[wife_name]
        elif husband_name := person.get("husband"):
            target_person.husband = Person.people[husband_name]

    return list(Person.people.values())
