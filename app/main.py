class Person:
    people: dict = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:

    for person_info in people:
        Person(person_info["name"], person_info["age"])

    for person_info in people:
        person = Person.people[person_info["name"]]

        if person_info.get("wife"):
            person.wife = Person.people[person_info["wife"]]
            person.wife.husband = person

    return list(Person.people.values())
