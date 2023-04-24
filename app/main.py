class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = list()
    for person in people:
        if None in person.values():
            person_list.append(Person(person["name"], person["age"]))
        else:
            new_person = Person(person["name"], person["age"])
            if "wife" in person:
                new_person.wife = person["wife"]
            else:
                new_person.husband = person["husband"]
            person_list.append(new_person)

    for person in person_list:
        if "wife" in dir(person):
            person.wife = Person.people[person.wife]
        elif "husband" in dir(person):
            person.husband = Person.people[person.husband]
    return person_list
