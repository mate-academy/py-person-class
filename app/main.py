class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(human["name"], human["age"]) for human in people]

    index = 0
    for human in people:
        if "wife" in human and human["wife"]:
            result_list[index].wife = Person.people[human["wife"]]
        elif "husband" in human and human["husband"]:
            result_list[index].husband = Person.people[human["husband"]]
        index += 1

    return result_list
