class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = []

    for human in people:
        person_object = Person(human["name"], human["age"])

        if "wife" in human:
            if human["wife"] is not None:
                person_object.wife = human["wife"]
        elif "husband" in human:
            if human["husband"] is not None:
                person_object.husband = human["husband"]

        person_list.append(person_object)
    for pers in Person.people:
        if "wife" in dir(Person.people[pers]):
            p_p_link = Person.people[pers]
            p_p_link.wife = Person.people[Person.people[pers].wife]
        elif "husband" in dir(Person.people[pers]):
            p_p_link = Person.people[pers]
            p_p_link.husband = Person.people[Person.people[pers].husband]

    return person_list
