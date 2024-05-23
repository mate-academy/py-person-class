class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for one in people:
        person = Person(one["name"], one["age"])
        if ("wife" in one and one["wife"] is not None
                and one["wife"] in Person.people):
            person.wife = Person.people[one["wife"]]
            person.wife.husband = person
        elif ("husband" in one and one["husband"] is not None
              and one["husband"] in Person.people):
            person.husband = Person.people[one["husband"]]
            person.husband.wife = person
        person_list.append(person)
    return person_list
