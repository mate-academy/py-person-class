class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for pers in people:
        name = pers["name"]
        age = pers["age"]
        person = Person(name, age)

        if "wife" in pers and pers["wife"] is not None:
            wife_name = pers["wife"]
            wife = Person.people.get(wife_name)
            if wife:
                person.wife = wife
                wife.husband = person

        if "husband" in pers and pers["husband"] is not None:
            husband_name = pers["husband"]
            husband = Person.people.get(husband_name)
            if husband:
                person.husband = husband
                husband.wife = person

        person_list.append(person)

    return person_list
