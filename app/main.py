class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for dict_person in people:
        person = Person(dict_person["name"], dict_person["age"])
        person_list.append(person)

    for dict_person in people:
        person_ref = Person.people[dict_person["name"]]

        if ("wife" in dict_person.keys()
                and dict_person["wife"] is not None):
            person_ref.wife = Person.people[dict_person["wife"]]
        if ("husband" in dict_person.keys()
                and dict_person["husband"] is not None):
            person_ref.husband = Person.people[dict_person["husband"]]

    return person_list
