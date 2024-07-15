class Person:

    people = {}

    def __init__(self, name: str, age: float) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    index = 0
    res_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if person.get("wife") and person["wife"]:
            res_list[index].wife = Person.people[person["wife"]]
        elif person.get("husband") and person["husband"]:
            res_list[index].husband = Person.people[person["husband"]]
        index += 1

    return res_list
