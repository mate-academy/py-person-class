class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(args: list) -> list:
    result_list = []

    for per in args:
        Person(per["name"], per["age"])

    for per in args:
        person = Person.people[per["name"]]
        if per.get("wife"):
            person.wife = Person.people[per["wife"]]
        elif per.get("husband"):
            person.husband = Person.people[per["husband"]]
        result_list.append(person)
    return result_list
