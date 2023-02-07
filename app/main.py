class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person_info in people:
        if person_info.get("wife"):
            Person.people[person_info["name"]].wife = (
                Person.people[person_info["wife"]]
            )
        if person_info.get("husband"):
            Person.people[person_info["name"]].husband = (
                Person.people[person_info["husband"]]
            )
    return person_list
