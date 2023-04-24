class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_objects = [Person(person["name"], person["age"])
                      for person in people]

    for person in people:
        if person.get("wife"):
            person_with_wife = Person.people[person["name"]]
            person_with_wife.wife = Person.people[person["wife"]]

        elif person.get("husband"):
            person_with_husband = Person.people[person["name"]]
            person_with_husband.husband = Person.people[person["husband"]]

    return person_objects
