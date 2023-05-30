class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_ls = []

    for person in people:
        persons_ls.append(Person(person["name"], person["age"]))

    for person in people:
        current_person = Person.people[person["name"]]

        if "wife" in person.keys() and person["wife"]:
            current_person.wife = Person.people[person["wife"]]

        if "husband" in person.keys() and person["husband"]:
            current_person.husband = Person.people[person["husband"]]

    return persons_ls
