class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = {human["name"]: Person(human["name"], human["age"])
                        for human in people}
    for human in people:
        person = person_instances[human["name"]]
        if human.get("wife") is not None:
            person.wife = person_instances[human["wife"]]
        elif human.get("husband") is not None:
            person.husband = person_instances[human["husband"]]
    return list(person_instances.values())
