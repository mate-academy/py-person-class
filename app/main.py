class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        person = Person(name, age)
    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]
        if "wife" in person_data and person_data["wife"] is not None:
            partner_name = person_data["wife"]
            partner = Person.people[partner_name]
            person.wife = partner
            partner.husband = person
        elif "husband" in person_data and person_data["husband"] is not None:
            partner_name = person_data["husband"]
            partner = Person.people[partner_name]
            person.husband = partner
            partner.wife = person
        people_list.append(person)
    return people_list
