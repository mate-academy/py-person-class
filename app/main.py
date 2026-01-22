class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people_data: list) -> list:
    result = []

    for human in people_data:
        result.append(Person(human["name"], human["age"]))

    for human in people_data:
        human_keys = human.keys()
        if "wife" in human_keys and human["wife"]:
            Person.people[human["name"]].wife = Person.people[human["wife"]]
        if "husband" in human_keys and human["husband"]:
            Person.people[human["name"]].husband = (
                Person.people
            )[human["husband"]]

    return result
