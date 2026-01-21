class Person:
    people = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [Person(person["name"], person["age"])for person in people]
    for person in people:
        iterable_person = Person.people[person["name"]]
        if "wife" in person and person["wife"] is not None:
            iterable_person.wife = Person.people[person["wife"]]
        elif "husband" in person and person["husband"] is not None:
            iterable_person.husband = Person.people[person["husband"]]    
    return persons_list
