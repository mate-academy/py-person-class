class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_created_people = []
    for person in people:
        inst_person = Person(person["name"], person["age"])
        if "wife" in person.keys():
            partner = "wife"
        else:
            partner = "husband"
        list_of_created_people.append(inst_person)
        if person[partner] in Person.people.keys():
            name = person[partner]
            if partner == "wife":
                inst_person.wife = Person.people[name]
                Person.people[name].husband = inst_person
            else:
                inst_person.husband = Person.people[name]
                Person.people[name].wife = inst_person
    return list_of_created_people
