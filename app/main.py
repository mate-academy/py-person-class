class Person:

    people = {}

    def __init__(self, name, age):
        self.age = age
        self.name = name
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    lst_of_perps = [Person(person["name"], person["age"]) for person in people]

    for i in people:
        if "wife" in i and i["wife"] is not None:
            wife = Person.people[i["wife"]]
            Person.people[i["name"]].wife = wife

        elif "husband" in i and i["husband"] is not None:
            husband = Person.people[i["husband"]]
            Person.people[i["name"]].husband = husband

    return lst_of_perps
