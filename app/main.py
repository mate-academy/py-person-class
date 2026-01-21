class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [Person(h.get("name"), h.get("age")) for h in people]
    for human in people:
        instance = Person.people.get(human.get("name"))
        wife_name = human.get("wife")
        husband_name = human.get("husband")
        if wife_name:
            instance.wife = Person.people.get(wife_name)
        if husband_name:
            instance.husband = Person.people.get(husband_name)

    return person_instances
