class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        (Person(new_person["name"], new_person["age"]))
        for new_person in people
    ]
    for person in people:
        if person.get("wife"):
            person_list[people.index(person)].wife \
                = Person.people[person["wife"]]
        elif person.get("husband"):
            person_list[people.index(person)].husband \
                = Person.people[person["husband"]]
    return person_list
