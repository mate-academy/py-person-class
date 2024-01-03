class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = list()
    for person_data in people:
        person = Person(person_data["name"], person_data["age"])
    for person in people:
        tmp = Person.people[person["name"]]
        if "wife" in person:
            if person["wife"]:
                tmp.wife = Person.people[person["wife"]]
        elif "husband" in person:
            if person["husband"]:
                tmp.husband = Person.people[person["husband"]]
        person_list.append(tmp)
    return person_list
