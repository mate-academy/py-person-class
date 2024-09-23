class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(people[i]["name"],
                   people[i]["age"])
                   for i in range(len(people))]

    for i, person in enumerate(people_list):
        if people[i].get("wife"):
            person.wife = Person.people.get(people[i]["wife"])
        elif people[i].get("husband"):
            person.husband = Person.people.get(people[i]["husband"])
    return people_list



