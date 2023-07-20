class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person_data in people:
        person = Person(person_data.get("name"), person_data.get("age"))
        person_list.append(person)

    for person_data in people:
        name = person_data.get("name")
        person = Person.people[name]

        if person_data.get("wife"):
            person.wife = Person.people[person_data.get("wife")]
        elif person_data.get("husband"):
            person.husband = Person.people[person_data.get("husband")]

    return person_list
