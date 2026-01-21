class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list[dict]) -> list[Person]:

    Person.people.clear()
    person_list = [Person(person["name"]
                          , person["age"]) for person in people]

    for person_dict in people:

        wife_name = person_dict.get("wife")
        if wife_name is not None and wife_name in Person.people:
            Person.people[person_dict["name"]].wife \
                = Person.people[person_dict["wife"]]
        husband_name = person_dict.get("husband")
        if husband_name is not None and husband_name in Person.people:
            Person.people[person_dict["name"]].husband \
                = Person.people[person_dict["husband"]]
    return person_list
