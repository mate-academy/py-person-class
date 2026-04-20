class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = [Person(person.get("name"),
                          person.get("age")) for person in people]
    for person in people:
        human = Person.people[person.get("name")]
        wife_name = person.get("wife")
        if wife_name is not None:
            human.wife = Person.people[wife_name]
        husband_name = person.get("husband")
        if husband_name is not None:
            human.husband = Person.people[husband_name]
    return person_list
