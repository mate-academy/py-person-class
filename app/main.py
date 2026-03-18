class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        if self.name not in Person.people.keys():
            Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_instances = [Person(p["name"], p["age"]) for p in people]

    for person in people:
        current_person = Person.people[person["name"]]

        if person.get("wife") is not None:
            wife_name = person["wife"]
            current_person.wife = Person.people[wife_name]

        elif person.get("husband") is not None:
            husband_name = person["husband"]
            current_person.husband = Person.people[husband_name]

    return person_instances
