class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        __class__.people[self.name] = self


def create_person_list(peoples: list) -> list:
    list_result = [Person(member["name"], member["age"]) for member in peoples]

    for index, member in enumerate(peoples):
        if "wife" in member:
            for pos in range(len(peoples)):
                if list_result[pos].name == member["wife"]:
                    list_result[index].wife = list_result[pos]
        if "husband" in member:
            for pos in range(len(peoples)):
                if list_result[pos].name == member["husband"]:
                    list_result[index].husband = list_result[pos]

    return list_result
