class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.setdefault(name, self)


def create_person_list(people: list[Person]) -> list[Person]:
    person_list = []

    for people_dict in people:
        person = Person(people_dict["name"], people_dict["age"])
        person_list.append(person)

    for ind, spouses in enumerate(people):
        if "wife" in spouses and spouses["wife"] is not None:
            wife = Person.people.get(spouses["wife"])
            person_list[ind].wife = wife
            wife.husband = person_list[ind]
        if "husband" in spouses and spouses["husband"] is not None:
            husband = Person.people.get(spouses["husband"])
            person_list[ind].husband = Person.people.get(spouses["husband"])
            husband.wife = person_list[ind]
    return person_list
