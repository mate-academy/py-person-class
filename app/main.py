class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list[Person]:
    for person in people:
        Person(person["name"], person["age"])

    for person in people:
        if "wife" in person and person["wife"]:
            person_obj = Person.people.get(person["name"])
            person_obj.wife = Person.people.get(person["wife"])
        elif "husband" in person and person["husband"]:
            person_obj = Person.people.get(person["name"])
            person_obj.husband = Person.people.get(person["husband"])

    return list(Person.people.values())
