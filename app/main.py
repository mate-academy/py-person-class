class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    instances = {}

    for person in people:
        person_instance = Person(person["name"], person["age"])
        instances[person["name"]] = person_instance

    for person in people:
        if "wife" in person and person["wife"]:
            partner_name = person["wife"]
            instances[person["name"]].wife = instances.get(partner_name)
        elif "husband" in person and person["husband"]:
            partner_name = person["husband"]
            instances[person["name"]].husband = instances.get(partner_name)

    return list((instances.values()))
