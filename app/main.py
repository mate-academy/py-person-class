class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    for data in people:
        Person(data["name"], data["age"])

    for data in people:
        person = Person.people[data["name"]]

        if "wife" in data and data["wife"] is not None:
            partner_name = data["wife"]
            partner = Person.people[partner_name]
            person.wife = partner

        elif "husband" in data and data["husband"] is not None:
            partner_name = data["husband"]
            partner = Person.people[partner_name]
            person.husband = partner

    return list(Person.people.values())
