class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result = []
    for person in people:
        result.append(Person(person["name"], person["age"]))

    for i, person_dict in enumerate(people):
        person_obj = result[i]
        if person_dict.get("wife"):
            person_obj.wife = Person.people[person_dict["wife"]]
        elif person_dict.get("husband"):
            person_obj.husband = Person.people[person_dict["husband"]]

    return result
