class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[str(self.name)] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        result.append(Person(person["name"], person["age"]))

    for person in people:
        if "wife" in person.keys():
            for partner in result:
                if partner.name == person["name"]:
                    for spouse in result:
                        if spouse.name == person["wife"]:
                            partner.wife = spouse
                            spouse.husband = partner
    return result
