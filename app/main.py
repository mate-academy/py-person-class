class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_instances = {}
    for person_info in people:
        person_name = person_info["name"]
        person = Person(person_name, person_info["age"])
        person_instances[person_name] = person

    for person_info in people:
        person_name = person_info["name"]
        if "wife" in person_info and person_info["wife"] is not None:
            person_instances[person_name].wife \
                = person_instances[person_info["wife"]]
        if "husband" in person_info and person_info["husband"] is not None:
            person_instances[person_name].husband \
                = person_instances[person_info["husband"]]

    return list(person_instances.values())
