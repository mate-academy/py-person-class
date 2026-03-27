class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people = {}
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person in people:
        person_instance = Person.people[person["name"]]
        wife = person.get("wife")
        if wife:
            person_instance.wife = Person.people[wife]
        husband = person.get("husband")
        if husband:
            person_instance.husband = Person.people[husband]
    return person_list
