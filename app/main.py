class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for person in people:
        human = Person(
            name=person["name"],
            age=person["age"],
        )
        result_list.append(human)
    for person in people:
        human = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            human.wife = Person.people.get(person["wife"])
        if "husband" in person and person["husband"]:
            human.husband = Person.people.get(person["husband"])
    return result_list
