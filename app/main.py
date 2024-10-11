class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int
    ) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for person in people:
        persons.append(Person(person["name"], person["age"]))

    for person in people:
        if "wife" in person and person["wife"]:
            wife = person["wife"]
            Person.people[person["name"]].wife = Person.people[wife]
        if "husband" in person and person["husband"]:
            husband = person["husband"]
            Person.people[person["name"]].husband = Person.people[husband]

    return persons
