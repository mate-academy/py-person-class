class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"]) for person in people]
    for person_dict, person_instance in zip(people, person_list):
        wife = person_dict.get("wife")
        husband = person_dict.get("husband")
        if wife:
            person_instance.wife = Person.people[wife]
        if husband:
            person_instance.husband = Person.people[husband]
    return person_list
