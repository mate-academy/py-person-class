class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    for person_dict in people:
        Person(person_dict["name"], person_dict["age"])
    for person_dict in people:
        person_obj = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            person_obj.wife = Person.people[person_dict["wife"]]
        if person_dict.get("husband"):
            person_obj.husband = Person.people[person_dict["husband"]]

    return [Person.people[p["name"]] for p in people]
