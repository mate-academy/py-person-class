class Person:
    people = {}

    def __init__(self, name: str, age: int, ) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = [Person(person["name"], person["age"]) for person in people]
    for i in range(len(people)):
        for person in result:
            if (people[i].get("husband")
                    and people[i]["husband"] == person.name):
                result[i].husband = person
            if people[i].get("wife") and people[i]["wife"] == person.name:
                result[i].wife = person
    return result
