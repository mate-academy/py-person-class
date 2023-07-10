class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people_list: list) -> list:
    person_list = []
    for i in range(len(people_list)):
        human = Person(people_list[i]["name"], people_list[i]["age"])
        if "wife" in people_list[i].keys() \
                and people_list[i]["wife"] is not None:
            human.wife = people_list[i]["wife"]
        elif "husband" in people_list[i].keys() \
                and people_list[i]["husband"] is not None:
            human.husband = people_list[i]["husband"]
        person_list.append(human)

    for person in person_list:
        if "wife" in person.__dict__.keys():
            if person.wife in Person.people.keys():
                person.wife = Person.people[person.wife]
        if "husband" in person.__dict__.keys():
            if person.husband in Person.people.keys():
                person.husband = Person.people[person.husband]

    return person_list
