class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_data = [Person(name=d["name"], age=d["age"]) for d in people]
    for index, value in enumerate(people):
        if value.get("wife"):
            person_data[index].wife = Person.people[value["wife"]]
        elif value.get("husband"):
            person_data[index].husband = Person.people[value["husband"]]
    return person_data
