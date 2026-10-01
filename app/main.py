class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    Person.people.clear()

    person_instances = [
        Person(name=p["name"], age=p["age"])
        for p in people_data
    ]

    for person_dict in people_data:
        person = Person.people[person_dict["name"]]

        if person_dict.get("wife"):
            person.wife = Person.people[person_dict["wife"]]
        elif person_dict.get("husband"):
            person.husband = Person.people[person_dict["husband"]]

    return person_instances
