class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for person_data in people:
        person = Person.people[person_data["name"]]

        if wife := person_data.get("wife"):
            person.wife = Person.people[wife]
        elif husband := person_data.get("husband"):
            person.husband = Person.people[husband]

    return persons
