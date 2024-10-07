class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_lst: list[dict]) -> list[Person]:
    people_obj = [
        Person(person["name"], person["age"]) for person in people_lst
    ]
    for index, person in enumerate(people_lst):
        if person.get("wife"):
            people_obj[index].wife = Person.people[person["wife"]]
        elif person.get("husband"):
            people_obj[index].husband = Person.people[
                person["husband"]
            ]
    return people_obj
