class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]

    for index, person in enumerate(people):
        if "wife" in person:
            wife = Person.people.get(person["wife"])
            if wife:
                person_list[index].wife = wife
        if "husband" in person:
            husband = Person.people.get(person["husband"])
            if husband:
                person_list[index].husband = husband

    return person_list
