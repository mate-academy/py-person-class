class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:  # List[dict] -> List[Person]
    for person in people:
        love_key = "husband" if "husband" in person else "wife"
        name = person["name"]
        age = person["age"]

        if person[love_key]:
            Person(name, age).__dict__[love_key] = person[love_key]
        else:
            Person(name, age)

    for person in Person.people.values():
        love_key = "husband" if "husband" in person.__dict__ else "wife"

        if love_key in person.__dict__:
            love = Person.people[person.__dict__[love_key]]
            person.__dict__[love_key] = love

    return list(Person.people.values())
