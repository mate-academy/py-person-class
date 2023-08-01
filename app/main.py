class Person:

    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        person_instance = Person(person["name"], person["age"])
        if person.get("wife"):
            person_instance.wife = person["wife"]
        if person.get("husband"):
            person_instance.husband = person["husband"]

    persons_instance = [person_link for person_link in Person.people.values()]

    for person in persons_instance:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]
        if hasattr(person, "husband"):
            person.husband = Person.people[person.husband]

    return persons_instance
