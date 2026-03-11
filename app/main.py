class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    people_inst = [Person(person["name"], person["age"]) for person in people]

    for i in range(len(people_inst)):
        for person in people_inst:
            if people[i].get("wife") == person.name:
                people_inst[i].wife = person
            elif people[i].get("husband") == person.name:
                people_inst[i].husband = person

    return people_inst
