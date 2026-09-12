class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    dc = []
    for pep in people:
        pop = Person(name=pep["name"], age=pep["age"])
        dc.append(pop)

    for pep in people:
        if pep.get("wife"):
            pers = Person.people.get(pep["name"])
            wf = Person.people.get(pep["wife"])
            pers.wife = wf

        if pep.get("husband"):
            pers = Person.people.get(pep["name"])
            hsb = Person.people.get(pep["husband"])
            pers.husband = hsb

    return dc
