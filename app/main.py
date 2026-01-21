class Person:
    people = {}

    def __init__(self, name: str, age: int, **kwargs) -> None:
        self.name = name
        self.age = age
        if (wife := kwargs.get("wife")):
            self.wife = wife
        elif (husband := kwargs.get("husband")):
            self.husband = husband
        Person.people[name] = self


def create_person_list(people: list) -> list:
    human_list = []
    for person in people:
        human_list.append(Person(
            person["name"],
            person["age"],
            wife=person.get("wife"),
            husband=person.get("husband")))

    for person in people:
        obj = Person.people.get(person.get("name"))
        if (wife_name := person.get("wife")):
            obj.wife = Person.people.get(wife_name)
        elif (husband_name := person.get("husband")):
            obj.husband = Person.people.get(husband_name)

    return human_list
