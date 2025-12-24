class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: dict) -> list:
    person_list = []
    for pers in people:
        person = Person(pers["name"], pers["age"])
        if "wife" in pers and pers["wife"] is not None:
            for i in people:
                if i["name"] == pers["wife"]:
                    person.wife = Person(i["name"], i["age"])
            person.wife.husband = person
        elif "husband" in pers and pers["husband"] is not None:
            person.husband = Person.people[pers["husband"]]
            person.husband.wife = person

        person_list.append(person)

    return person_list
