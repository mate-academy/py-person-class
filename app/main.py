class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = []
    result = {}
    for person in people:
        name = person["name"]
        age = person["age"]
        person = Person(name, age)
        persons.append(person)
    for item in people:
        person = Person.people[item["name"]]
        if item.get("wife"):
            wife = Person.people[item["wife"]]
            person.wife = wife
        if item.get("husband"):
            husband = Person.people[item["husband"]]
            person.husband = husband
    return persons
