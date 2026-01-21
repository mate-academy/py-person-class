class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = [
        Person(person_list["name"],
               person_list["age"]) for person_list in people
    ]

    for person_dict in people:
        person_name = person_dict["name"]
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            Person.people[person_name].wife = Person.people[wife_name]

        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            Person.people[person_name].husband = Person.people[husband_name]

    return person_instances
