class Person:
    people = {}

    def __init__(self, name: str, age: int) -> any:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    personal_ls = [
        Person(person_dict["name"], person_dict["age"])
        for person_dict in people
    ]

    for person_dict in people:
        name = person_dict["name"]
        if person_dict.get("wife"):
            Person.people[name].wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband"):
            Person.people[name].husband = Person.people[person_dict["husband"]]

    return personal_ls
