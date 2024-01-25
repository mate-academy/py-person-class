class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        self.__class__.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        if "wife" in person and person["wife"] in Person.people:
            wife = Person.people[person["wife"]]
            husband = Person.people[person["name"]]

            wife.husband = husband
            husband.wife = wife

        if "husband" in person and person["husband"] in Person.people:
            wife = Person.people[person["name"]]
            husband = Person.people[person["husband"]]

            wife.husband = husband
            husband.wife = wife

    return [person for person in Person.people.values()]
