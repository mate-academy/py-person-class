class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = [Person(person_data["name"], person_data["age"])
                   for person_data in people]

    for person_data in people:
        person = Person.people.get(person_data["name"])
        if person_data.get("wife") and person_data["wife"]:
            person.wife = Person.people.get(person_data["wife"])
        elif person_data.get("husband") and person_data["husband"]:
            person.husband = Person.people.get(person_data["husband"])

    return people_list
