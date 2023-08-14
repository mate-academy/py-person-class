class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for person_dict in people:
        name = person_dict["name"]
        wife_name = person_dict.get("wife")
        if wife_name:
            wife_name = person_dict["wife"]
            person = Person.people[name]
            wife = Person.people[wife_name]
            person.wife = wife
            wife.husband = person

    return person_list
