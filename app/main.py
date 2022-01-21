class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for item in people:
        result.append(Person(item["name"], item["age"]))
    for item in people:
        if "wife" in item and item["wife"] is not None:
            Person.people[item["name"]].wife = Person.people[item["wife"]]
        elif "husband" in item and item["husband"] is not None:
            Person.people[item["name"]].husband = Person.people[
                item["husband"]
            ]
    return result
