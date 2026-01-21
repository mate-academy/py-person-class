class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person_dict["name"], person_dict["age"])
                   for person_dict in people
                   ]

    for person_dict in people:
        name = person_dict["name"]
        person = Person.people[name]
        if person_dict.get("wife"):
            wife = person_dict["wife"]
            person.wife = Person.people[wife]
        if person_dict.get("husband"):
            husband = person_dict["husband"]
            person.husband = Person.people[husband]
    return person_list
