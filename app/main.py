class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        if "wife" in kwargs and kwargs["wife"] is not None:
            self.wife = kwargs["wife"]
        if "husband" in kwargs and kwargs["husband"] is not None:
            self.husband = kwargs["husband"]
        Person.people[name] = self

def create_person_list(people: list) -> list:
    persons = []
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
        persons.append(person)

    for person_data in people:
        person = Person.people[person_data["name"]]
        if "wife" in person_data and person_data["wife"]:
            person.wife = Person.people.get(person_data["wife"])
        if "husband" in person_data and person_data["husband"]:
            person.husband = Person.people.get(person_data["husband"])

    return persons