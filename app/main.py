class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    people = [Person(person["name"], person["age"])
              for person in people_data]

    for index, part_of_list in enumerate(people_data):
        if part_of_list.get("wife"):
            people[index].wife = Person.people[
                part_of_list.get("wife")]

        if part_of_list.get("husband"):
            people[index].husband = Person.people[
                part_of_list.get("husband")]

    return people
