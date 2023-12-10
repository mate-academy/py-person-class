class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for element in people:
        result.append(Person(element["name"], element["age"]))

    for number in range(len(people)):
        keys_of_people = list(people[number].keys())
        if keys_of_people[2] == "wife" and people[number]["wife"] is not None:
            result[number].wife = Person.people[people[number]["wife"]]
        if (keys_of_people[2] == "husband"
                and people[number]["husband"] is not None):
            result[number].husband = Person.people[people[number]["husband"]]
    return result
