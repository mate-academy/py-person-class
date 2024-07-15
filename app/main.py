class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:

    person_list = []

    for one in people:
        name = one["name"]
        new_person = Person(name, one["age"])
        Person.people[name] = new_person

        name_wife = one.get("wife")
        if name_wife is not None:
            if Person.people.get(name_wife) is None:
                new_person.wife = name_wife
            else:
                new_person.wife = Person.people.get(name_wife)
                Person.people[name_wife].husband = Person.people.get(name)

        name_husband = one.get("husband")
        if name_husband is not None:
            if Person.people.get(name_husband) is None:
                new_person.husband = name_husband
            else:
                new_person.husband = Person.people.get(name_husband)
                Person.people[name_husband].wife = Person.people.get(name)

        person_list.append(new_person)
        Person.people[name] = new_person

    return person_list
