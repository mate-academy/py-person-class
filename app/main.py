class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    result = {}
    for person in people:
        result[person["name"]] = Person(list(person.items())[0][1],
                                        list(person.items())[1][1])
    for human in people:
        if human.get("husband") is not None:
            result[human["name"]].husband = result[human.get("husband")]
        elif human.get("wife") is not None:
            result[human["name"]].wife = result[human.get("wife")]

    Person.people = result
    return list(result.values())
