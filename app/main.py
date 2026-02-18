class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [
        Person(person.get("name"), person.get("age"))
        for person in people
    ]
    for person in people:
        person_obj = Person.people.get(person.get("name"))
        if person.get("wife"):
            person_obj.wife = Person.people.get(person.get(
                "wife"))
        elif person.get("husband"):
            person_obj.husband = Person.people.get(person.get(
                "husband"))
    return person_list
