class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_object = []
    for item in people:
        list_of_object.append(Person(item["name"], item["age"]))

    for persons in people:
        person = Person.people[persons["name"]]
        if persons.get("wife") is not None:
            person.wife = Person.people[persons["wife"]]
        if persons.get("husband") is not None:
            person.husband = Person.people[persons["husband"]]
    return list_of_object
