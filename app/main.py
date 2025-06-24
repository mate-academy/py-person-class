class Person:
    people ={}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self
def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = []
    for p in people:
        person = Person(name=p["name"], age=p["age"])
        person_list.append(person)

    for i, p in enumerate(people):
        person = person_list[i]

        if "wife" in p and p["wife"] is not None:
            person.wife = Person.people[p["wife"]]
        if "husband" in p and p["husband"] is not None:
            person.husband = Person.people[p["husband"]]
    return person_list
