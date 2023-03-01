class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for index, person in enumerate(people):
        result.append(Person(person["name"], person["age"]))
        if person.get("wife") and person["wife"] in Person.people:
            result[index].wife = Person.people[person["wife"]]
            Person.people[person["wife"]].husband = result[index]
        elif person.get("husband") and person["husband"] in Person.people:
            result[index].husband = Person.people[person["husband"]]
            Person.people[person["husband"]].wife = result[index]
    return result
