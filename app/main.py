class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(persons: list[dict]) -> list[Person]:

    persons_instances = [Person(person["name"], person["age"])
                         for person in persons]

    for i in range(len(persons_instances)):
        if "wife" in persons[i] and persons[i]["wife"] is not None:
            persons_instances[i].wife = Person.people[persons[i]["wife"]]

        elif "husband" in persons[i] and persons[i]["husband"] is not None:
            persons_instances[i].husband = Person.people[persons[i]["husband"]]

    return persons_instances
