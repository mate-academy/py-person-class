class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_object = [Person(person.get("name"),
                            person.get("age")) for person in people]
    for person in people:
        name = person.get("name")
        obj = Person.people[name]

        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if wife_name is not None:
            obj.wife = Person.people.get(wife_name)
        if husband_name is not None:
            obj.husband = Person.people.get(husband_name)
    return person_object
