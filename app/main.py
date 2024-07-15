class Person:

    people = {}

    def __init__(self, name: str, age: float) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    res_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if person.get("wife") and person["wife"]:
            res_list[person].wife = Person.people[person["wife"]]
        elif person.get("husband") and person["husband"]:
            res_list[person].husband = Person.people[person["husband"]]

    return res_list
