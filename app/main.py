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

    people_ex = [Person(**item) for item in people]

    for person in people_ex:
        if hasattr(person, "wife") and isinstance(person.wife, str):
            wife = Person.people.get(person.wife)
            if wife:
                person.wife = wife
                wife.husband = person

    return people_ex
