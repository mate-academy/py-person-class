class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    persons_list = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        if person.get("wife") and Person.people.get(person["wife"]):
            wife = Person.people[person["wife"]]
            husband = Person.people[person["name"]]

            wife.husband = husband
            husband.wife = wife

        if person.get("husband") and Person.people.get(person["husband"]):
            wife = Person.people[person["name"]]
            husband = Person.people[person["husband"]]

            wife.husband = husband
            husband.wife = wife

    return persons_list
