class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    person_list = [Person(human["name"], human["age"]) for human in people]
    dict_for_merge = {el.name: el for el in person_list}
    Person.people |= dict_for_merge

    for human in people:
        if human.get("wife", None) is not None:
            husband = next(
                (el for el in person_list if el.name == human["name"]), None)
            wife = next(
                (el for el in person_list if el.name == human["name"]), None)

            if husband and wife:
                husband.wife = wife
                wife.husband = husband

    return person_list
