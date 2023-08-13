class Person:
    people: dict[str, "Person"] = {}

    def __init__(self, name: str, age: int) -> None:
        self.name: str = name
        self.age: int = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_lst: list[Person] = [
        Person(person["name"], person["age"])
        for person in people
    ]
    for person in people:
        if person.get("wife"):
            main_person = Person.people[person["name"]]
            person_wife = Person.people[person["wife"]]
            main_person.wife = person_wife
        elif person.get("husband"):
            main_person = Person.people[person["name"]]
            person_husband = Person.people[person["husband"]]
            main_person.husband = person_husband

    return person_lst
