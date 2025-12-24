class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result_output = [Person(person["name"], person["age"]) for person in people]
    for i, person in enumerate(people):
        if person.get("wife"):
            result_output[i].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            result_output[i].husband = Person.people[person["husband"]]
    return result_output
