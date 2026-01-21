class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [
        Person(name=person["name"],
               age=person["age"])
        for person in people
    ]

    for person in people:
        person_obj = Person.people[person["name"]]
        if person.get("wife") is not None:
            person_obj.wife = Person.people[person["wife"]]
            Person.people[person["wife"]].husband = person_obj

        if person.get("husband") is not None:
            person_obj.husband = Person.people[person["husband"]]
            Person.people[person["husband"]].wife = person_obj

    return persons
