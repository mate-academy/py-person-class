class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = []
    for person_dict in people_list:
        person_instances.append(Person(name=person_dict["name"],
                                       age=person_dict["age"]))

    for person_dict in people_list:
        current_person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"]:
            current_person.wife = Person.people.get(person_dict["wife"])
        if "husband" in person_dict and person_dict["husband"]:
            current_person.husband = Person.people.get(person_dict["husband"])
    return person_instances
