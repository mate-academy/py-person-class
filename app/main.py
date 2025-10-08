class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people: list) -> list:
    Person_people = []
    for man in people:
        unit = Person(man["name"], man["age"])
        Person_people.append(unit)
    for man1 in people:
        if man1.get("wife") != None:
            Person.people[man1["name"]].wife = Person.people[man1["wife"]]
        else:
            if man1.get("husband") != None:
                Person.people[man1["name"]].husband = Person.people[man1["husband"]]
            else:
                pass
    return Person_people
