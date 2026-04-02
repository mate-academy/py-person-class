class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    Person.people.clear()
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        person_list.append(new_person)
    for person in people:
        current_person = Person.people[person["name"]]
        if person.get("wife"):
            current_person.wife = Person.people.get(person["wife"])
        elif person.get("husband"):
            current_person.husband = Person.people.get(person["husband"])
    return person_list
