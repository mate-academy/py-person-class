class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    result_list = [Person(person["name"], person["age"]) for person in people]

    i = 0
    for person in people:
        if person.get("wife"):
            result_list[i].wife = Person.people[person.get("wife")]
            i += 1
        elif person.get("husband"):
            result_list[i].husband = Person.people[person.get("husband")]
            i += 1
        else:
            i += 1

    return result_list
