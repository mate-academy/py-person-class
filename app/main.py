class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self
        self.spouse = None


def create_person_list(people_data: list) -> list:
    Person.people.clear()

    for p in people_data:
        Person(p.get('name'), p.get('age'))

    for p in people_data:
        current_person = Person.people.get(p.get('name'))
        if current_person:
            spouse_name = p.get('wife') or p.get('husband')
            current_person.spouse = Person.people.get(spouse_name)

    return [Person.people.get(p.get('name')) for p in people_data]
