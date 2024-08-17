class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:

    list_of_people = [Person(person["name"],
                             person["age"])
                      for person in people]

    for person in range(len(people)):

        if "husband" in people[person] and people[person]["husband"]:
            list_of_people[person].husband = (
                Person.people)[people[person]["husband"]]

        elif "wife" in people[person] and people[person]["wife"]:
            list_of_people[person].wife = (
                Person.people)[people[person]["wife"]]

    return list_of_people
