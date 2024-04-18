class Person:
    people = {}

    def __init__(self, name: str, age: int, spouse: str = None) -> None:
        self.name = name
        self.age = age
        self.spouse = None
        Person.people[name] = self
        if spouse:
            self.spouse = Person.people.get(spouse)


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        new_person = Person(person["name"], person["age"]
                            , person.get["wife"] or person.get("husband"))
        person_list.append(new_person)
    return person_list
