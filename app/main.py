class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_info["name"], person_info["age"])
        for person_info in people
    ]

    for index, person_info in enumerate(people):
        if person_info.get("wife") is not None:
            person_list[index].wife = Person.people[person_info["wife"]]
        elif person_info.get("husband") is not None:
            person_list[index].husband = Person.people[person_info["husband"]]

    return person_list
