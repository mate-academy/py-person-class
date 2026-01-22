class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list[dict]) -> list[Person]:
    result = []
    for person in people:
        Person(name=person["name"], age=person["age"])
    for person in people:
        if person.get("husband"):
            Person.people.get(person.get("name")).husband =\
                Person.people.get(person.get("husband"))
        elif person.get("wife"):
            Person.people.get(person.get("name")).wife = \
                Person.people.get(person.get("wife"))
        result.append(Person.people[person["name"]])
    return result
