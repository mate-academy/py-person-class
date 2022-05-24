class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def add_person(self):
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    new_people = []
    for person_dict in people:
        person = Person(person_dict["name"], person_dict["age"])
        person.add_person()
        new_people.append(person)

    for i, new_person in enumerate(new_people):
        if "wife" in people[i].keys() and people[i]["wife"]:
            name_wife = people[i]["wife"]
            new_person.wife = new_person.people[name_wife]

        elif "husband" in people[i].keys() and people[i]["husband"]:
            name_husband = people[i]["husband"]
            new_person.husband = \
                new_person.people[name_husband]
    return new_people
