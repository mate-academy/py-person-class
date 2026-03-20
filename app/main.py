class Person:
    people = {}

    def __init__(self, name : str, age : int) -> None:
        self.name = name
        self.age = age
        self.people.update({name : self})


def create_person_list(people: list) -> list:

    result_list = []
    result_list = [Person(p["name"], p["age"]) for p in people]
    for partner in people:
        person = Person.people[partner["name"]]

        if partner.get("wife") is not None:
            person.wife = Person.people.get(partner["wife"])

        if partner.get("husband") is not None:
            person.husband = Person.people.get(partner["husband"])

    return result_list
