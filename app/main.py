class Person:

    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person in people:
        person_instance = Person(
            name=person["name"],
            age=person["age"]
        )
        person_instances.append(person_instance)

    for person in people:
        if not person.get("wife") is None is person.get("husband"):
            instance_spouse_link = Person.people[list(person.values())[2]]
            if list(person.keys())[2] != "wife":
                Person.people[person["name"]].husband = instance_spouse_link
            else:
                Person.people[person["name"]].wife = instance_spouse_link
    return person_instances
