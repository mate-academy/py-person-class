class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_data: list) -> list:
    people = [Person(person["name"], person["age"])
              for person in people_data]

    for index, person in enumerate(people_data):
        if person.get("wife"):
            people[index].wife = Person.people[
                person.get("wife")]

        if person.get("husband"):
            people[index].husband = Person.people[
                person.get("husband")]

    return people
