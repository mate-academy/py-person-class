class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = []
    for person_dict in people:
        person_instance = Person(person_dict["name"], person_dict["age"])
        result.append(person_instance)
    for person_dict in people:
        person = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            wife_name = person_dict["wife"]
            person.wife = Person.people[wife_name]
        if person_dict.get("husband"):
            husband_name = person_dict["husband"]
            person.husband = Person.people[husband_name]
    return result
