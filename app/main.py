class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))

    for person in people:
        name = person.get("name")
        wife = person.get("wife")
        husband = person.get("husband")
        if wife:
            Person.people.get(name).wife = Person.people.get(wife)
        if husband:
            Person.people.get(name).husband = Person.people.get(husband)
    return person_list
