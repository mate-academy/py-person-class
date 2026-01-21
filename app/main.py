class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    humans = [Person(person["name"], person["age"]) for person in people]

    for person in people:
        human = Person.people.get(person["name"])

        if "wife" in person and person["wife"]:
            wife = Person.people.get(person["wife"])

            if wife:
                wife.husband = human
                human.wife = wife

        if "husband" in person and person["husband"]:
            husband = Person.people.get(person["husband"])

            if husband:
                husband.wife = human
                human.husband = husband

    return humans
