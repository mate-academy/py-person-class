class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    result = []

    result = [Person(person_dict["name"],
                     person_dict["age"]) for person_dict in people
              ]

    for person_dict in people:
        name = person_dict["name"]
        person_object = Person.people[name]

        wife = person_dict.get("wife")
        husband = person_dict.get("husband")

        if wife is not None and wife in Person.people:
            person_object.wife = Person.people[wife]
            Person.people[wife].husband = person_object
        if husband is not None and husband in Person.people:
            person_object.husband = Person.people[husband]
            Person.people[husband].wife = person_object

    return result
