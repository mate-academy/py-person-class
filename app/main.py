class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [
        Person(person_data["name"], person_data["age"])
        for person_data in people
    ]
    for i in range(len(people)):
        if people[i].get("wife"):
            result[i].wife = Person.people.get(people[i].get("wife"))
        if people[i].get("husband"):
            result[i].husband = Person.people.get(people[i].get("husband"))
    return result
