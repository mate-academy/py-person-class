
class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for element in people:
        person_example = Person(
            name=element["name"],
            age=element["age"],
        )
    for element in people:
        person_example = Person.people.get(element["name"])
        wife = element.get("wife")
        husband = element.get("husband")
        if wife is not None:
            person_example.wife = Person.people[wife]
        if husband is not None:
            person_example.husband = Person.people[husband]
        result.append(person_example)
    return result
