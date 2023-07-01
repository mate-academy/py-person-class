class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for one_person in people:
        person = Person(one_person["name"], one_person["age"])
        person_list.append(person)

    for one_person in people:
        person = Person.people[one_person["name"]]
        if "wife" in one_person and one_person["wife"] is not None:
            person.wife = Person.people[one_person["wife"]]
            person.wife.husband = person
        elif "husband" in one_person and one_person["husband"] is not None:
            person.husband = Person.people[one_person["husband"]]
            person.husband.wife = person

    return person_list
