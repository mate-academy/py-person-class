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
        if person.get("husband") is None and person.get("wife") is None:
            continue
        else:
            if "wife" in person:
                Person.people[person.get("name")].wife\
                    = Person.people[person.get("wife")]
            elif "husband" in person:
                Person.people[person.get("name")].husband\
                    = Person.people[person.get("husband")]
    return person_list
