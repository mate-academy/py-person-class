class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({name: self})


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for index in range(len(people)):
        spouse = "wife" if "wife" in people[index] else "husband"
        if people[index][spouse]:
            person_list[index].__setattr__(
                spouse,
                Person.people.get(people[index][spouse])
            )

    return person_list
