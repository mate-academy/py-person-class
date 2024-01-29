class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    list_of_person = [Person(person["name"],
                             person["age"]) for person in people]
    for i, person in enumerate(people):
        if person.get("husband"):
            husband_name = person["husband"]
            list_of_person[i].husband = Person.people[husband_name]
        elif person.get("wife"):
            wife_name = person["wife"]
            list_of_person[i].wife = Person.people[wife_name]
    return list_of_person
