class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    instances = [Person(name=info["name"], age=info["age"]) for info in people]

    for person in people:
        current = Person.people[person["name"]]
        wife_name = person.get("wife")
        if wife_name:
            current.wife = Person.people[wife_name]
        husband_name = person.get("husband")
        if husband_name:
            current.husband = Person.people[husband_name]

    return instances
