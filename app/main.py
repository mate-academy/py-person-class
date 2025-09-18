class Person:
    people: dict = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people_list: list) -> list:
    new_person_list = [Person(person["name"], person["age"])
                       for person in people_list]

    for index, person in enumerate(people_list):
        related_persons = Person.people

        if person.get("wife"):
            new_person_list[index].wife = related_persons[person["wife"]]

        if person.get("husband"):
            new_person_list[index].husband = related_persons[person["husband"]]

    return new_person_list
