class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_persons = []
    mari_list = ["wife", "husband"]
    for humain in people:
        person = Person(humain["name"], humain["age"])
        for mari in mari_list:
            if humain.get(mari) and humain[mari]:
                setattr(person, mari, humain[mari])
        list_persons.append(person)

    for person in list_persons:
        for mari in mari_list:
            if getattr(person, mari, None):
                for person_2 in list_persons:
                    if person_2.name == getattr(person, mari):
                        setattr(person, mari, person_2)
                        break

    return list_persons
