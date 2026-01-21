class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person_data in people:
        name = person_data.get("name")
        age = person_data.get("age")
        person_instance = Person(name, age)
        person_instances.append(person_instance)

    for person_data in people:
        person_instance = Person.people[person_data["name"]]
        if husband_name := person_data.get("husband"):
            person_instance.husband = Person.people[husband_name]
        if wife_name := person_data.get("wife"):
            person_instance.wife = Person.people[wife_name]

    return person_instances
