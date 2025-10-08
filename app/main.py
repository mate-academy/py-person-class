class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people: list[dict]) -> list[Person]:
    person_list = [Person(p.get("name"), p.get("age")) for p in people]
    for p1 in people:
        if p1.get("wife") != None:
            Person.people[p1.get("name")].wife = Person.people[p1.get("wife")]
        elif p1.get("husband") != None:
            Person.people[p1.get("name")].husband = Person.people[p1.get("husband")]
        else:
            pass
    return person_list
