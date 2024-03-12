class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    total_list = [Person(info["name"], info["age"]) for info in people]

    for info in people:
        result = Person.people.get(info["name"])

        if info.get("wife") and info["wife"] is not None :
            result.wife = Person.people.get(info["wife"])
        elif info.get("husband") and info["husband"] is not None:
            result.husband = Person.people.get(info["husband"])

    return total_list
