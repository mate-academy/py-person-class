class Person:

    people = {}  # {name : Person}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()  # clear Person.people dict from previous items

    [Person(person["name"], person["age"])
     for person in people]  # creating Persons

    for person in people:
        if person.get("wife") is not None:
            Person.people[person["name"]].wife\
                = Person.people[person.get("wife")]
        if person.get("husband") is not None:
            Person.people[person["name"]].husband\
                = Person.people[person.get("husband")]
    return [person for person in Person.people.values()]
