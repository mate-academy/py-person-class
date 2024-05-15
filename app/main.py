class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person.get("name"), person.get("age")))
    for person in people:
        if "wife" in person and person.get("wife"):
            husband = Person.people.get(person.get("name"))
            husband.wife = Person.people.get(person.get("wife"))
        elif "husband" in person and person.get("husband"):
            wife = Person.people.get(person.get("name"))
            wife.husband = Person.people.get(person.get("husband"))
    return person_list
