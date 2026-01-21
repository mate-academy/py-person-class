class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for index, person in enumerate(people):
        partner = person_list[index]

        if person.get("wife"):
            wife = Person.people[person["wife"]]
            partner.wife = wife
        if person.get("husband"):
            husband = Person.people[person["husband"]]
            partner.husband = husband

    return person_list
