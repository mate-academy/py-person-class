class Person:
    people: dict = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list[Person]:
    person_list: list[Person] = []
    for person in people:
        # next line initiates the creation of an instance of the class
        Person(person["name"], person["age"])
        person_list.append(Person.people[person["name"]])
    pers_dict = Person.people
    for person in people:
        if person.get("wife") is not None:
            pers_dict[person["name"]].wife = pers_dict[person["wife"]]
        elif person.get("husband") is not None:
            pers_dict[person["name"]].husband = pers_dict[person["husband"]]

    return person_list
