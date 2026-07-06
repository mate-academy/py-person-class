class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife"):
            wife_ref = Person.people.get(person["wife"])
            Person.people[person["name"]].wife = wife_ref
        if person.get("husband"):
            husband_ref = Person.people.get(person["husband"])
            Person.people[person["name"]].husband = husband_ref
    class_people = [person for person in Person.people.values()]
    return class_people
