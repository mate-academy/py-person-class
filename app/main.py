class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person_instances.append(Person(name, age))

    for person_data in people:
        if person_data.get("wife"):
            wife_name = person_data["wife"]
            Person.people[person_data["name"]].wife = Person.people[wife_name]

        if person_data.get("husband"):
            husband_name = person_data["husband"]
            Person.people[person_data["name"]].husband \
                = Person.people[husband_name]
    return person_instances
