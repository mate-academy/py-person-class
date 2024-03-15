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
        key = list({"wife", "husband"}.intersection(set(person.keys())))[0]
        list_of_created_people.append(inst_person)
        if person[key] in Person.people.keys():
            name = person[key]
            if key == "wife":
                inst_person.wife = Person.people[name]
                Person.people[name].husband = inst_person
            else:
                inst_person.husband = Person.people[name]
                Person.people[name].wife = inst_person
    return list_of_created_people
