class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    person_list = [Person(indiv["name"], indiv["age"]) for indiv in people]
    for individ in people:
        wife = individ.get("wife")
        if wife in Person.people:
            Person.people[individ["name"]].wife = Person.people[wife]
            Person.people[wife].husband = Person.people[individ["name"]]

    return person_list
