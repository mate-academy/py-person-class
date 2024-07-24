class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self

    def set_relationships(self, wife: str = None, husband: str = None) -> None:
        if wife:
            self.wife = Person.people[wife]
        if husband:
            self.husband = Person.people[husband]


def create_person_list(people: list) -> list:
    person_objects = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for person_dict in people:
        name = person_dict["name"]
        wife = person_dict.get("wife")
        husband = person_dict.get("husband")

        person = Person.people[name]
        person.set_relationships(wife, husband)

    return person_objects
