class Person:
    people = {}

    def __init__(self, name : str, age : int) -> None :
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = [(Person(person["name"], person["age"]))
                    for person in people]

    for index, person in enumerate(people):
        if person.get("wife") is not None:
            name_wife = person.get("wife")
            persons_list[index].wife = Person.people.get(name_wife)
        elif person.get("husband") is not None:
            name_husband = person.get("husband")
            persons_list[index].husband = Person.people.get(name_husband)

    return persons_list
