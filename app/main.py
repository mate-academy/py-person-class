class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.age = age
        self.name = name
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person1 = Person(person["name"], person["age"])

        if "wife" in person and person["wife"]:
            person1.wife = Person.people[person["name"]]
            Person.people[person["name"]].husband = person1
        if "husband" in person and person["husband"]:
            person1.husband = Person.people[person["name"]]
            Person.people[person["name"]].wife = person1

        person_list.append(persongit commit -am 'Solution'1)
    return person_list
