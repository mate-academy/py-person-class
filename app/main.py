class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_instances = []
    for person in people:
        people_instances.append(Person(person["name"], person["age"]))

    for index, person in enumerate(people):
        if "wife" in person and person["wife"] is not None:
            wife_name = person["wife"]
            if wife_name in Person.people:
                people_instances[index].wife = Person.people[wife_name]
        if "husband" in person and person["husband"] is not None:
            husband_name = person["husband"]
            if husband_name in Person.people:
                people_instances[index].husband = Person.people[husband_name]
    return people_instances
