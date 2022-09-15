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

    for person in Person.people:
        person_object = Person.people[person]

        if "wife" in dir(Person.people[person]):
            wife_name = Person.people[person].wife
            person_object.wife = Person.people[wife_name]
        elif "husband" in dir(Person.people[person]):
            husband_name = Person.people[person].husband
            person_object.husband = Person.people[husband_name]

    return person_list
