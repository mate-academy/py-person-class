class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    ls_people = []
    for man in people:
        name = man["name"]
        age = man["age"]
        wife = man.get("wife")
        husband = man.get("husband")
        person = Person(name, age)
        if wife:
            person.wife = wife
        elif husband:
            person.husband = husband
        ls_people.append(person)
    for man in ls_people:
        if hasattr(man, "wife"):
            man.wife = Person.people[man.wife]
        elif hasattr(man, "husband"):
            man.husband = Person.people[man.husband]
    return ls_people
