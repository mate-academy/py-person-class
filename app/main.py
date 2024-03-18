class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    def get_instance(name: str) -> Person:
        for person in person_instances:
            if person.name == name:
                return person

    person_instances = [
        Person(person["name"], person["age"])
        for person in people
    ]

    for index, person in enumerate(people):
        if person.get("wife", None) is not None:
            person_instances[index].wife = get_instance(person["wife"])
        if person.get("husband", None) is not None:
            person_instances[index].husband = get_instance(person["husband"])

    return person_instances
