class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    person_list = []
    for person in people:
        person_obj = Person(person["name"], person["age"])
        person_list.append(person_obj)
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = (
                Person.people)[person.get("wife")]
        if person.get("husband"):
            Person.people[person["name"]].husband = (
                Person.people)[person.get("husband")]
    return person_list
