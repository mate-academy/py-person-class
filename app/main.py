class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people.update({self.name: self})


def create_person_list(people_list: list) -> list:
    for dict_people in people_list:
        Person(dict_people["name"], dict_people["age"])

    for dict_people in people_list:
        if "wife" in dict_people and dict_people["wife"] is not None:
            setattr(
                Person.people[dict_people["name"]],
                "wife",
                Person.people[dict_people["wife"]]
            )
        if "husband" in dict_people and dict_people["husband"] is not None:
            setattr(
                Person.people[dict_people["name"]],
                "husband",
                Person.people[dict_people["husband"]]
            )
    person_list = [Person.people[key] for key in Person.people]
    return person_list
