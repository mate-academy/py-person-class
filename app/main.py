class Person:

    people = {}

    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)
        Person.people[name] = self

def create_person_list(people: list) -> list:

    Person.people = {}

    people_ex = []
    for item in people:
        person = Person(**item)
        people_ex.append(person)

    for person in people_ex:
        for item in people_ex:
            if hasattr(person, "wife") and isinstance(person.wife, str) and item.name == person.wife:
                person.wife = item
            elif hasattr(person, "husband") and isinstance(person.husband, str) and item.name == person.husband:
                person.husband = item

    return people_ex
