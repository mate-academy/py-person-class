class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

    @classmethod
    def pick_by_name(cls, in_name: str) -> object:
        for person in Person.people:
            if person == in_name:
                return Person.people[person]


def create_person_list(people: list) -> list:
    instances_ls = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        pair = person.get("wife") or person.get("husband")
        name = person["name"]
        if pair and "wife" in person:
            Person.pick_by_name(name).wife = Person.pick_by_name(pair)
        elif pair and "husband" in person:
            Person.pick_by_name(name).husband = Person.pick_by_name(pair)
    return instances_ls
