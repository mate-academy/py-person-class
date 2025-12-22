class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = []
    for person in people:
        list_of_people.append(Person(person["name"], person["age"]))
        if "wife" in person:
            if person["wife"] is not None:
                list_of_people[-1].wife = person["wife"]
        else:
            if person["husband"] is not None:
                list_of_people[-1].husband = person["husband"]

    for person in list_of_people:
        if hasattr(person, "wife"):
            if person.wife in Person.people:
                person.wife = Person.people[person.wife]
        if hasattr(person, "husband"):
            if person.husband in Person.people:
                person.husband = Person.people[person.husband]

    return list_of_people
