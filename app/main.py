class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    [
        Person(
            person_dict["name"], person_dict["age"]
        )
        for person_dict in people_list
    ]


    for person_dict in people_list:
        person = Person.people[person_dict["name"]]
        if "wife" in person_dict and person_dict["wife"]:
            person.wife = Person.people[person_dict["wife"]]
            person.wife.husband = person
        elif "husband" in person_dict and person_dict["husband"]:
            person.husband = Person.people[person_dict["husband"]]
            person.husband.wife = person

    return list(Person.people.values())
