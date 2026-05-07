class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    instances = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        instances.append(person)

    for instance, person_dict in zip(instances, people):
        if person_dict.get("wife"):
            wife_name = person_dict["wife"]
            instance.wife = Person.people[wife_name]

        if person_dict.get("husband"):
            husband_name = person_dict["husband"]
            instance.husband = Person.people[husband_name]

    return instances
