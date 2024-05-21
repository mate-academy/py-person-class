class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = [Person(person_dict["name"],
                          person_dict["age"])
                   for person_dict in people]

    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if person_dict and person_dict.get("wife"):
            person.wife = Person.people[person_dict["wife"]]
        if person_dict and person_dict.get("husband"):
            person.husband = Person.people[person_dict["husband"]]

    return person_list
