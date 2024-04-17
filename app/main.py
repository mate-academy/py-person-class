class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Add the instance to the class attribute `people`
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for human in people:
        person_instance = Person(name=human["name"], age=human["age"])
        person_instances.append(person_instance)

    for human in people:
        if human.get("wife"):
            Person.people[human["name"]].wife = \
                Person.people[human["wife"]]
        elif human.get("husband"):
            Person.people[human["name"]].husband = \
                Person.people[human["husband"]]
    return person_instances
