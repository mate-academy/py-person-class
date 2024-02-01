class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    people_instances = [Person(person["name"],
                               person["age"]) for person in people]
    for i, person in enumerate(people):
        if person.get("husband"):
            husband_name = person["husband"]
            Person.people[person["name"]].husband = Person.people[husband_name]
        elif person.get("wife"):
            wife_name = person["wife"]
            people_instances[i].wife = Person.people[wife_name]
    return people_instances
