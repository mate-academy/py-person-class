class Person:
    people = {}

    def __init__(self, name: str, age: int, *args, **kwargs) -> None:
        self.name = name
        self.age = age
        self.wife = kwargs.get("wife")
        self.husband = kwargs.get("husband")

        self.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(**person) for person in people if person]

    for person in result:
        if person.husband:
            person.husband = Person.people[person.husband]
        elif person.wife:
            person.wife = Person.people[person.wife]
        else:
            del person.wife
            del person.husband

    return result
