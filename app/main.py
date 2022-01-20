class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(singel_person["name"], singel_person["age"])
                   for singel_person in people]

    for singel_person in people:
        if "wife" in singel_person and singel_person["wife"] is not None:
            Person.people[singel_person["name"]].wife \
                = Person.people[singel_person["wife"]]

        if "husband" in singel_person and singel_person["husband"] is not None:
            Person.people[singel_person["name"]].husband \
                = Person.people[singel_person["husband"]]

    return people_list
