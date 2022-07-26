class Person:
    people = {}

    def __int__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [Person(name=name["name"],
                             age=name["age"]) for name in people]

    for person in people:
        if "wife" in person:
            if person["wife"] is not None:
                Person.people[person["name"]].wife = \
                    Person.people[person["wife"]]
        if "husband" in person:
            if person["husband"] is not None:
                Person.people[person["name"]].husband = \
                    Person.people[person["husband"]]

    return list_of_people
