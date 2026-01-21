class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(peoples: list) -> list:
    person_list = []
    for pers in peoples:
        person = Person(pers["name"], pers["age"])
        person_list.append(person)
    for pers in peoples:
        person = Person.people[pers["name"]]
        if "wife" in pers and pers["wife"] is not None:
            wife = Person.people.get(pers["wife"])
            if wife:
                setattr(person, "wife", wife)
            else:
                setattr(person, "wife", None)
        if "husband" in pers and pers["husband"] is not None:
            husband = Person.people.get(pers["husband"])
            if husband:
                setattr(person, "husband", husband)
            else:
                setattr(person, "husband", None)
    return person_list
