class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(name=person.get("name"),
                                  age=person.get("age")))
    for person in people:
        if person.get("wife"):
            Person.people[person.get("name")].wife\
                = Person.people[person.get("wife")]
        elif person.get("husband"):
            Person.people[person.get("name")].husband\
                = Person.people[person.get("husband")]
    return person_list
