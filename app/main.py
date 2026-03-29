class Person:
    people = {}

    def __init__(self,
                 name: str,
                 age: int) -> None:

        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(persons: list) -> list:
    Person.people = {}
    temp_person = [Person(person["name"], person["age"]) for person in persons]

    for person in persons:
        if person.get("wife") is not None:
            person_wife = Person.people[person["wife"]]
            Person.people[person["name"]].wife = person_wife

        elif person.get("husband") is not None:
            person_husband = Person.people[person["husband"]]
            Person.people[person["name"]].husband = person_husband

    return temp_person
