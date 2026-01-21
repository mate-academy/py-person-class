class Person:
    people = {}
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

        
def create_person_list(people: list) -> list:
    Person.people = {}
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        instance = Person.people[person["name"]]
        if "wife" in person and person["wife"]:
            instance.wife = Person.people[person["wife"]]
        if "husband" in person and person["husband"]:
            instance.husband = Person.people[person["husband"]]
    return list(Person.people.values())
