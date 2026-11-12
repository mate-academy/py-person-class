class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self
def create_person_list(people: list) -> list:
    person_list = [Person(p["name"], p["age"]) for p in people]
    for p in people:
        person = Person.people[p["name"]]
        if "wife" in p and p["wife"]:
            person.wife = Person.people[p["wife"]]
        if "husband" in p and p["husband"]:
            person.husband = Person.people[p["husband"]]
    return person_list
