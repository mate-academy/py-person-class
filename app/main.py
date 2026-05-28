class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = [
        Person(name=person["name"], age=person["age"]) for person in people
    ]

    for person in people:
        person_obj = Person.people[person["name"]]

        if person.get("wife"):
            wife_name = person["wife"]
            person_obj.wife = Person.people[wife_name]

        if person.get("husband"):
            husband_name = person["husband"]
            person_obj.husband = Person.people[husband_name]

    return result_list
