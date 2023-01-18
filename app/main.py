class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    personal_list = [
        Person(one_people["name"], one_people["age"]) for one_people in people
    ]

    for one_people in people:
        if "wife" in one_people and one_people["wife"] is not None:
            Person.people[one_people["name"]].wife\
                = Person.people[one_people["wife"]]

        if "husband" in one_people and one_people["husband"] is not None:
            Person.people[one_people["name"]].husband\
                = Person.people[one_people["husband"]]

    return personal_list
