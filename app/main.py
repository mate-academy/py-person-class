class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_specimen = [Person(person["name"],
                              person["age"]) for person in people]
    for one_person in people:
        if "wife" in one_person and one_person["wife"]:
            Person.people[one_person["name"]].wife =\
                Person.people[one_person["wife"]]
        if "husband" in one_person and one_person["husband"]:
            Person.people[one_person["name"]].husband =\
                Person.people[one_person["husband"]]
    return people_specimen
