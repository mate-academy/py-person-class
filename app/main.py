class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(person["name"], person["age"]) for person in people]
    for el in people:
        if el.get("wife"):
            Person.people[el.get("wife")].husband = Person.people[el["name"]]
            Person.people[el["name"]].wife = Person.people[el.get("wife")]
    return result_list
