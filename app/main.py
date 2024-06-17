class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []

    for person_dict in people:
        name = person_dict["name"]
        age = person_dict["age"]
        person_instance = Person(name=name, age=age)
        person_instances.append(person_instance)

    for person_dict in people:
        name = person_dict["name"]
        spouse_name = person_dict.get("wife") or person_dict.get("husband")

        if spouse_name:
            person_instance = Person.people[name]
            spouse_instance = Person.people[spouse_name]

            if "wife" in person_dict and person_dict["wife"]:
                person_instance.wife = spouse_instance
            if "husband" in person_dict and person_dict["husband"]:
                person_instance.husband = spouse_instance
    return person_instances
