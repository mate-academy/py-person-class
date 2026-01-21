class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self
    pass


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []
    for person in people:
        name = person["name"]
        age = person["age"]
        new_person = Person(name, age)
        person_list.append(new_person)
    for person in people:
        current_person = Person.people[person["name"]]
        if person.get("wife"):
            current_person.wife = Person.people[person["wife"]]

        if person.get("husband"):
            current_person.husband = Person.people[person["husband"]]

    return person_list

    pass
