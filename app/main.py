class Person():

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    person_list = [Person(p["name"], p["age"]) for p in people]

    people_map = Person.people

    for person_dict, person_instance in zip(people, person_list):
        if person_dict.get("wife"):
            person_instance.wife = people_map.get(person_dict["wife"])
        if person_dict.get("husband"):
            person_instance.husband = people_map.get(person_dict["husband"])

    return person_list
