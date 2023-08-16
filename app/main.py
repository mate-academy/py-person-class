class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list:
    for person in people:
        person_info = list(person.values())
        Person(person_info[0], person_info[1])
    for person in people:
        if "wife" in person:
            if person["wife"] is not None:
                person_link = list(person.values())[0]
                husband = Person.people[person_link]
                husband.wife = Person.people[person["wife"]]
        if "husband" in person:
            if person["husband"] is not None:
                person_link = list(person.values())[0]
                wife = Person.people[person_link]
                wife.husband = Person.people[person["husband"]]
    return list(Person.people.values())
