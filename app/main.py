class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for current_person in range(len(people_list)):
        if (people_list[current_person].name
                == people[current_person]["name"]):

            if people[current_person].get("wife"):
                people_list[current_person].wife = Person.people[
                    people[current_person]["wife"]]

            if people[current_person].get("husband"):
                people_list[current_person].husband = Person.people[
                    people[current_person]["husband"]]
    return people_list
