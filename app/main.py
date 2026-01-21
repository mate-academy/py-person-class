class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for human in people:
        result.append(Person(human["name"], human["age"]))
    for person_index in range(len(people)):
        if people[person_index].get("wife") is not None:
            wife = people[person_index].get("wife")
            result[person_index].wife = Person.people[wife]
        if people[person_index].get("husband") is not None:
            husband = people[person_index].get("husband")
            result[person_index].husband = Person.people[husband]

    return result
