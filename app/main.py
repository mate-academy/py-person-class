class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self  # Store instance by name


def create_person_list(people: list) -> list:
    person_instances = {person_info["name"]: Person(person_info["name"],
                        person_info["age"]) for person_info in people}

    for person in people:
        person_instance = person_instances[person["name"]]
        if person.get("wife"):
            setattr(person_instance, "wife", person_instances[person["wife"]])
        if person.get("husband"):
            setattr(person_instance, "husband",
                    person_instances[person["husband"]])

    return list(person_instances.values())
