class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:

    person_instances = []

    for person_dict in people_list:
        name = person_dict["name"]
        age = person_dict["age"]
        person = Person(name, age)
        person_instances.append(person)

    for person_dict in people_list:
        name = person_dict["name"]
        person = Person.people[name]
        if "wife" in person_dict and person_dict["wife"]:
            person.wife = Person.people[person_dict["wife"]]
        elif "husband" in person_dict and person_dict["husband"]:
            person.husband = Person.people[person_dict["husband"]]

    return person_instances
