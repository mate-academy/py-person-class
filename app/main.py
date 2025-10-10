class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:

    person_list = [Person(person["name"], person["age"]) for person in people]

    person_index = 0
    for person in people:
        person_obj = person_list[person_index]
        if person.get("wife"):
            person_obj.wife = Person.people[person["wife"]]
        if person.get("husband"):
            person_obj.husband = Person.people[person["husband"]]
        person_index += 1

    return person_list
