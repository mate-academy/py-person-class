class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_instances = [Person(person["name"], person["age"])
                        for person in people
                        ]

    for human in people:
        person = Person.people[human["name"]]
        if human.get("wife"):
            person.wife = Person.people.get(human["wife"])
        if human.get("husband"):
            person.husband = Person.people.get(human["husband"])
    return person_instances
