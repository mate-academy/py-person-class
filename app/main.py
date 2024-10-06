class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:

    [Person(person["name"], person["age"]) for person in people]

    for person in people:
        person_instance = Person.people[person["name"]]

        if "wife" in person and person.get("wife"):
            person_instance.wife = Person.people[person["wife"]]
        elif "husband" in person and person.get("husband"):
            person_instance.husband = Person.people[person["husband"]]

    return list(Person.people.values())
