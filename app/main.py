class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:

    result = []

    for human in people:
        person = Person(human["name"], human["age"])
        result.append(person)

    for result_index, human in enumerate(people):

        if "wife" in human and human["wife"] is not None:
            wife_name = human["wife"]
            if wife_name in Person.people:
                result[result_index].wife = Person.people[wife_name]

        if "husband" in human and human["husband"] is not None:
            husband_name = human["husband"]
            if husband_name in Person.people:
                result[result_index].husband = Person.people[husband_name]

    return result
