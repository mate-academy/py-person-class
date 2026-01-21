class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_instances_list = [Person(person["name"], person["age"])
                             for person in people]

    for person in people:
        current_person = Person.people[person["name"]]
        partner_name = person.get("wife") or person.get("husband")
        if partner_name and person.get("wife"):
            partner_instance = Person.people[partner_name]
            current_person.wife = partner_instance
        elif partner_name and person.get("husband"):
            partner_instance = Person.people[partner_name]
            current_person.husband = partner_instance

    return person_instances_list
