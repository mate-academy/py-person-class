class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for list_person in people:
        person = Person(list_person.get("name"), list_person.get("age"))
        person_list.append(person)

    for list_person in people:
        if list_person.get("wife") is not None:
            person = Person.people.get(list_person.get("name"))
            spouse = Person.people.get(list_person.get("wife"))
            person.wife = spouse

        if list_person.get("husband") is not None:
            person = Person.people.get(list_person.get("name"))
            spouse = Person.people.get(list_person.get("husband"))
            person.husband = spouse

    return person_list
