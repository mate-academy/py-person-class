class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.create(self.name, self)

    @classmethod
    def create(cls, name: str, obj: Person) -> None:
        cls.people[name] = obj


def create_person_list(people: list) -> list:
    person_list = []

    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    count = 0
    for person in people:
        if "wife" in person and person["wife"] is not None:
            person_list[count].wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"] is not None:
            person_list[count].husband = Person.people[person["husband"]]
        count += 1

    return person_list
