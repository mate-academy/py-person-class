class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


people = []


def create_person_list(people: list) -> list:
    people_instances = [Person(person_data.get("name"), person_data.get("age"))
                        for person_data in people]

    for person_data in people:
        person = Person.people.get(person_data.get("name"))

        if person_data.get("wife"):
            person.wife = Person.people.get(person_data.get("wife"))

        if person_data.get("husband"):
            person.husband = Person.people.get(person_data.get("husband"))

    return people_instances
