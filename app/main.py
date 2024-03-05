class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    list_result = []

    for peopl in people:
        list_result.append(Person(peopl["name"], peopl["age"]))

    for i, peopl in enumerate(people):
        if "wife" in peopl:
            for pos in range(len(people)):
                if list_result[pos].name == peopl["wife"]:
                    list_result[i].wife = list_result[pos]
        if "husband" in peopl:
            for pos in range(len(people)):
                if list_result[pos].name == peopl["husband"]:
                    list_result[i].husband = list_result[pos]

    return list_result
