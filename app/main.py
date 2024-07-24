class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    res = {}
    for person in people:
        res[person["name"]] = Person(person["name"], person["age"])
    Person.people = res

    for person in people:
        if list(person.values())[2]:
            if person.get("wife"):
                Person.people[person["name"]].wife = res[person["wife"]]
            else:
                Person.people[person["name"]].husband = res[person["husband"]]

    res = list(res.values())
    return res
