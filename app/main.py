class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for persons in people:
        result_list.append(Person(persons.get("name"), persons.get("age")))
    for add_person in people:
        if add_person.get("wife"):
            Person.people[add_person.get("name")].wife = Person.people[
                add_person.get("wife")
            ]
        if add_person.get("husband"):
            Person.people[add_person.get("name")].husband = Person.people[
                add_person.get("husband")
            ]
    return result_list
