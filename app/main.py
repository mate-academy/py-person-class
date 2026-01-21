class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list[Person]:
    person_list = [Person(person_dict["name"], person_dict["age"])
                   for person_dict in people]

    for person_dict in people:
        if person_dict.get("wife"):
            Person.people[person_dict["name"]].wife = (
                Person.people)[person_dict["wife"]]
        elif person_dict.get("husband"):
            Person.people[person_dict["name"]].husband = (
                Person.people)[person_dict["husband"]]

    return person_list
