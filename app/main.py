class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:

    for person in people:
        new_person = Person(name=person.get("name"), age=person.get("age"))

        if wife := person.get("wife"):
            new_person.wife = wife

        if husband := person.get("husband"):
            new_person.husband = husband

    people_instances = Person.people.values()

    for person in people_instances:
        if hasattr(person, "wife"):
            wife = person.wife
            person.wife = Person.people.get(wife)
            continue

        if hasattr(person, "husband"):
            husband = person.husband
            person.husband = Person.people.get(husband)

    return list(people_instances)
