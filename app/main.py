class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_instances = []
    for person_list in people:
        name = person_list["name"]
        age = person_list["age"]
        person = Person(name, age)
        person_instances.append(person)

    for person_dict in people:
        person_name = person_dict["name"]
        if "wife" in person_dict and person_dict["wife"] is not None:
            wife_name = person_dict["wife"]
            Person.people[person_name].wife = Person.people[wife_name]
        elif hasattr(Person.people[person_name], "wife"):
            del Person.people[person_name].wife
        if "husband" in person_dict and person_dict["husband"] is not None:
            husband_name = person_dict["husband"]
            Person.people[person_name].husband = Person.people[husband_name]

    return person_instances
