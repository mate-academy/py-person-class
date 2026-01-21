class Person:

    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({name: self})


def create_person_list(people: list) -> list:

    result = [
        Person(elem["name"], elem["age"])
        for elem in people
    ]

    for elem in people:
        name = elem.get("name")
        wife = elem.get("wife")
        husband = elem.get("husband")
        if wife:
            Person.people.get(name).wife = Person.people.get(wife)
        elif husband:
            Person.people.get(name).husband = Person.people.get(husband)

    return result
