class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.partner_name = None
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    people_instance = [
        Person(name=person["name"], age=person["age"]) for person in people
    ]
    for index, person in enumerate(people):
        if person.get("wife") is not None:
            people_instance[index].wife = Person.people[person["wife"]]
        if person.get("husband") is not None:
            people_instance[index].husband = (Person.people)[person["husband"]]
    return people_instance
