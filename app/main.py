class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list:
    instances = []

    for person_data in people:
        new_person = Person(person_data["name"], person_data["age"])
        instances.append(new_person)

    for person_data in people:
        name = person_data["name"]
        current_instance = Person.people[name]

        if person_data.get("wife"):
            partner_name = person_data["wife"]
            current_instance.wife = Person.people[partner_name]

        elif person_data.get("husband"):
            partner_name = person_data["husband"]
            current_instance.husband = Person.people[partner_name]

    return instances
