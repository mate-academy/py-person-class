class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_dict in people:
        person = Person(name=person_dict["name"], age=person_dict["age"])
        person_instances.append(person)

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"]:
            person.wife = Person.people.get(person_dict["wife"])
        if "husband" in person_dict and person_dict["husband"]:
            person.husband = Person.people.get(person_dict["husband"])
    return person_instances
