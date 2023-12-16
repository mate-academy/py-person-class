class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_instances = [Person(name=person["name"], age=person["age"])
                   for person in people]

    for person in people:
        if person.get("wife"):
            main_person = Person.people[person["name"]]
            person_wife = Person.people[person["wife"]]
            main_person.wife = person_wife
        elif person.get("husband"):
            main_person = Person.people[person["name"]]
            person_husband = Person.people[person["husband"]]
            main_person.husband = person_husband

    return people_instances
