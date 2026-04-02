class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = []
    [
        person_list.append(Person(person["name"],
                                  person["age"])) for person in people
    ]
    for per in people:
        pers = Person.people[per["name"]]
        if per.get("wife") and per["wife"] is not None:
            pers.wife = Person.people.get(per["wife"])
        elif per.get("husband") and per["husband"] is not None:
            pers.husband = Person.people.get(per["husband"])
    return person_list
