class Person:

    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(name=each_one["name"], age=each_one["age"])
                   for each_one in people]

    for each_one in people:
        if "wife" in each_one and each_one["wife"] is not None:
            Person.people[each_one["name"]].wife = \
                Person.people[each_one["wife"]]

        if "husband" in each_one and each_one["husband"] is not None:
            Person.people[each_one["name"]].husband = \
                Person.people[each_one["husband"]]

    return result_list
