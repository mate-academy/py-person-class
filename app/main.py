class Person:
    people = {}

    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person_data["name"], person_data["age"]) for person_data in people]
    for person_data in people:
        result.append(Person(person_data["name"], person_data["age"]))
    for i, person_data in enumerate(people):
        if person_data.get("wife"):
            result[i].wife = Person.people[person_data["wife"]]
        elif person_data.get("husband"):
            result[i].husband = Person.people[person_data["husband"]]

    return result
