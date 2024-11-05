class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person["name"], person["age"]) for person in people]

    for index, person in enumerate(people):

        if person.get("wife"):
            wife = Person.people[person["wife"]]
            husband = people_list[index]

            husband.wife = wife
            wife.husband = husband

    return people_list
