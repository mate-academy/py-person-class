class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"])
        if person.get("wife"):
            new_person.wife = person.get("wife")
        if person.get("husband"):
            new_person.husband = person.get("husband")
        person_list.append(new_person)
    for person in person_list:
        if hasattr(person, "wife") and person.wife is not None:
            person.wife = Person.people[person.wife]
        if hasattr(person, "husband") and person.husband is not None:
            person.husband = Person.people[person.husband]
    return person_list
