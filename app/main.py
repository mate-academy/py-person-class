class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self

def create_person_list(people: list) -> list:
    Person.people.clear()
    people_objs = [Person(person_data["name"], person_data["age"]) for person_data in people]
    for person_data in people:
        if person_data.get("wife") is not None:
            person = Person.people[person_data["name"]]
            spouse = Person.people[person_data["wife"]]
            person.wife = spouse
        elif person_data.get("husband") is not None:
            person = Person.people[person_data["name"]]
            spouse = Person.people[person_data["husband"]]
            person.husband = spouse
    return people_objs
