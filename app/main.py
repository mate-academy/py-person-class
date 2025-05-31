class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people: list) -> list:
    for person_d in people:
        name = person_d["name"]
        age = person_d["age"]
        Person(name, age)

    for person_d in people:
        person = Person.people[person_d["name"]]
        wife_name = person_d.get("wife")
        if wife_name:
            person.wife = Person.people.get(wife_name)
        husband_name = person_d.get("husband")
        if husband_name:
            person.husband = Person.people.get(husband_name)
    return list(Person.people.values())
