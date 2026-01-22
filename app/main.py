class Person:
    people = {}

    def __init__(self, name, age):
        self.age = age
        self.name = name
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_humans = [Person(person["name"],
                             person["age"]) for person in people]

    for one_human in people:
        if "wife" in one_human and one_human["wife"] is not None:
            wife = Person.people[one_human["wife"]]
            Person.people[one_human["name"]].wife = wife

        elif "husband" in one_human and one_human["husband"] is not None:
            husband = Person.people[one_human["husband"]]
            Person.people[one_human["name"]].husband = husband

    return list_of_humans
