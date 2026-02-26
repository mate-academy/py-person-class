class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person.get("name"),
                          person.get("age")) for person in people]

    for i, person in enumerate(people):
        instance = person_list[i]
        wife = person.get("wife")
        husband = person.get("husband")
        if wife:
            instance.wife = Person.people.get(wife)
        if husband:
            instance.husband = Person.people.get(husband)
    return person_list
