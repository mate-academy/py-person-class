class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(men["name"], men["age"]) for men in people]

    for men in people:
        person = Person.people[men["name"]]
        if "wife" in men and men["wife"]:
            person.wife = Person.people.get(men["wife"])
        if "husband" in men and men["husband"]:
            person.husband = Person.people.get(men["husband"])
    return person_list
