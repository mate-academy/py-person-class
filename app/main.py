class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list[Person]:
    instances = {
        person["name"]: Person(person["name"], person["age"])
        for person in people
    }

    for person in people:
        if partner_name := person.get("wife"):
            instances[person["name"]].wife = instances.get(partner_name)
        elif partner_name := person.get("husband"):
            instances[person["name"]].husband = instances.get(partner_name)

    return list((instances.values()))
