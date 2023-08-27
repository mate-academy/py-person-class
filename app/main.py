class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    persons = []
    for human in people:
        name = human["name"]
        age = human["age"]
        pers = Person(name, age)

        if "wife" in human:
            wife_name = human["wife"]
            wife = Person.people.get(wife_name)
            if wife:
                pers.wife = wife
                wife.husband = pers

        if "husband" in human:
            husband_name = human["husband"]
            husband = Person.people.get(husband_name)
            if husband:
                pers.husband = husband
                husband.wife = pers
        persons.append(pers)

    return persons
