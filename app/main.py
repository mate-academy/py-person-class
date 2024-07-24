class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    res_arr = [Person(person["name"], person["age"]) for person in people]

    for i, person in enumerate(people):
        if person.get("wife"):
            res_arr[i].wife = Person.people[person["wife"]]
        if person.get("husband"):
            res_arr[i].husband = Person.people[person["husband"]]

    return res_arr
