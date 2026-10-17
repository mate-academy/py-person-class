class Person:

    people = {}

    def __init__(self, name : str, age : int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [Person(
        values["name"],
        values["age"]
    ) for values in people]

    for one_people in people:
        people_i = Person.people[one_people["name"]]
        if one_people.get("wife"):
            people_i.wife = Person.people[one_people["wife"]]
        if one_people.get("husband"):
            people_i.husband = Person.people[one_people["husband"]]

    return list_of_people
