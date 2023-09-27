class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for index, person in enumerate(people):
        partner = person_list[index]

        if person.get("wife"):
            wife = Person.people[person["wife"]]
            partner.wife = wife
        if person.get("husband"):
            husband = Person.people[person["husband"]]
            partner.husband = husband

    return person_list
