class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people_list: list) -> list:

    person_instances = []
    for person_data in people_list:
        name = person_data.get("name")
        age = person_data.get("age")
        person = Person(name, age)
        person_instances.append(person)

    for person_data in people_list:
        name = person_data.get("name")
        current_person = Person.people[name]

        if "wife" in person_data and person_data["wife"]:
            current_person.wife = Person.people[person_data["wife"]]
        else:
            delattr(current_person, "wife")
        if "husband" in person_data and person_data["husband"]:
            current_person.husband = Person.people[person_data["husband"]]
        else:
            delattr(current_person, "husband")

    return person_instances
