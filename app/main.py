class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_instances(people: list) -> None:
    for human in people:
        Person(human.get("name"), human.get("age"))


def create_person_list(people: list) -> list:
    create_instances(people)
    person_instances = [
        Person.people.get(human.get("name")) for human in people
    ]
    for human in people:
        for key in human:
            current_inst = Person.people.get(human.get("name"))
            if key == "wife" and human.get("wife") is not None:
                current_inst.wife = Person.people.get(human.get("wife"))
            elif key == "husband" and human.get("husband") is not None:
                current_inst.husband = Person.people.get(human.get("husband"))
    return person_instances
