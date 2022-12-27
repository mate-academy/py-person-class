class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        pers = Person(person["name"], person["age"])
        if "wife" in person and person["wife"]:
            pers.wife = person["wife"]
        if "husband" in person and person["husband"]:
            pers.husband = person["husband"]
        person_list.append(pers)
    for person in person_list:
        if "wife" in dir(person):
            person.wife = person.people[person.wife]
        if "husband" in dir(person):
            person.husband = person.people[person.husband]
    return person_list
