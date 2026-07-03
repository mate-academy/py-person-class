class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        if person.get("wife") and person["wife"]:
            Person.people[person["name"]].wife\
                = Person.people[person["wife"]]
        if person.get("husband") and person["husband"]:
            Person.people[person["name"]].husband\
                = Person.people[person["husband"]]

    return result_list
