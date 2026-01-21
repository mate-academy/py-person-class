class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    person_instances = {
        person["name"]: Person(person["name"], person["age"])
        for person in people
    }

    for person in people:
        current_person = person_instances[person["name"]]

        if "wife" in person:
            wife_name = person["wife"]
            if wife_name in person_instances:
                current_person.wife = person_instances[wife_name]

        if "husband" in person:
            husband_name = person["husband"]
            if husband_name in person_instances:
                current_person.husband = person_instances[husband_name]

    for person in person_instances.values():
        if person.wife is None:
            del person.wife
        if person.husband is None:
            del person.husband

    return list(person_instances.values())
