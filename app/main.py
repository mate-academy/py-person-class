class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self

    def set_wife(self, name: str) -> str:
        self.wife = self.people.get(name)
        return self.wife

    def set_husband(self, name: str) -> str:
        self.husband = self.people.get(name)
        return self.husband


def create_person_list(people: list) -> list:
    peoples = [
        (person, Person(person.get("name"), person.get("age"))) for person in people
    ]
    for info, person in peoples:
        if wife := info.get("wife"):
            person.set_wife(wife)
        elif husband := info.get("husband"):
            person.set_husband(husband)
    return [person[1] for person in peoples]
