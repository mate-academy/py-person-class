class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    Person.people = {}
    for person in people:
        ludi = Person(person["name"], person["age"])
        result.append(ludi)
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        elif person.get("husband") is not None:
            Person.people[person["name"]].husband =\
                Person.people[person["husband"]]
        else:
            pass
    return result
