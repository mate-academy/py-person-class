class Person:

    people = {}

    def __init__(self,
                 name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        Person(person["name"], person["age"])
    for person in people:
        pers = Person.people[person["name"]]
        if person.get("wife") and person["wife"] is not None:
            pers.wife = Person.people[person["wife"]]
            result.append(pers)
        elif person.get("husband") and person["husband"] is not None:
            pers.husband = Person.people[person["husband"]]
            result.append(pers)
        else:
            result.append(pers)
    return result
