class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [Person(person_dict["name"],
                          person_dict["age"]) for person_dict in people]
    for person_dict in people:
        if person_dict.get("wife"):
            person = Person.people[person_dict["wife"]]
            Person.people[person_dict["name"]].wife = person
        if person_dict.get("husband"):
            person = Person.people[person_dict["husband"]]
            Person.people[person_dict["name"]].husband = person
    return person_list
