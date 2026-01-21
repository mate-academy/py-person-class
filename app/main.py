class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    class_list = [
        Person(person_data["name"], person_data["age"])
        for person_data in people_data
    ]

    for person_data in people_data:
        if person_data.get("wife"):
            Person.people[person_data["name"]].wife = \
                Person.people[person_data["wife"]]

        if person_data.get("husband"):
            Person.people[person_data["name"]].husband = \
                Person.people[person_data["husband"]]

    return class_list
