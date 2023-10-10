class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [
        Person(person_data["name"],
               person_data["age"]) for person_data in people
    ]

    for person_data in people:
        if "wife" in person_data and person_data["wife"] in Person.people:
            person = Person.people[person_data["name"]]
            person.wife = Person.people[person_data["wife"]]
            Person.people[person_data["wife"]].husband = person
        elif "husband" in person_data and \
                person_data["husband"] in Person.people:
            person = Person.people[person_data["name"]]
            person.husband = Person.people[person_data["husband"]]
            Person.people[person_data["husband"]].wife = person

    return list_of_people
