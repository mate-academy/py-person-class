class Person:
    people = {}

    def __init__(
            self,
            name: str,
            age: int,

    ) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_humans = []
    for person in people:
        wife = None
        husband = None
        if "wife" in person:
            wife = person["wife"]
        elif "husband" in person:
            husband = person["husband"]
        mate = Person(person["name"], person["age"])
        mate.wife = wife
        mate.husband = husband
        list_of_humans.append(mate)

    for person in Person.people:
        if Person.people[person].wife:
            partner_name = Person.people[person].wife
            Person.people[person].wife = Person.people[partner_name]
            del Person.people[person].husband
        elif Person.people[person].husband:
            partner_name = Person.people[person].husband
            Person.people[person].husband = Person.people[partner_name]
            del Person.people[person].wife
        else:
            del Person.people[person].wife
            del Person.people[person].husband

    return list_of_humans
