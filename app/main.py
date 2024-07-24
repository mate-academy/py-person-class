class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    person_instances = []
    for person_dict in people_list:
        person = Person(person_dict["name"], person_dict["age"])
        person_instances.append(person)

    for person_dict in people_list:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"]:
            spouse = Person.people[person_dict["wife"]]
            person.wife = spouse
            spouse.husband = person
        elif "husband" in person_dict and person_dict["husband"]:
            spouse = Person.people[person_dict["husband"]]
            person.husband = spouse
            spouse.wife = person

    return person_instances
