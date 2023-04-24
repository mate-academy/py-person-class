class Person:

    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    for person in people:
        Person(person["name"], person["age"])
    list_of_peoples = list(Person.people.values())
    for num_people, inf_people in enumerate(list_of_peoples):
        if people[num_people].get("wife"):
            list_of_peoples[num_people].wife = Person.people.get(
                people[num_people]["wife"]
            )
        elif people[num_people].get("husband"):
            list_of_peoples[num_people].husband = Person.people.get(
                people[num_people]["husband"]
            )
    return list_of_peoples
