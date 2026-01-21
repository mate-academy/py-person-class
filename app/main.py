class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int,
    ) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(peoples: list) -> list:
    for data_person in peoples:
        Person(
            name=data_person["name"],
            age=data_person["age"]
        )

    for data_person in peoples:
        person = Person.people[data_person["name"]]

        if "wife" in data_person and data_person["wife"]:
            person.wife = Person.people[data_person["wife"]]

        if "husband" in data_person and data_person["husband"]:
            person.husband = Person.people[data_person["husband"]]

    return list(Person.people.values())
