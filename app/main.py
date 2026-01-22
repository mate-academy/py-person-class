class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name

        self.age = age
        Person.people[name] = self


def create_person_list(people_list: list) -> list:
    for person_data in people_list:
        Person(person_data["name"], person_data["age"])
    for person_data in people_list:
        person = Person.people[person_data["name"]]
        if person_data.get("husband"):
            person.husband = Person.people[person_data["husband"]]
        if person_data.get("wife") :
            person.wife = Person.people[person_data["wife"]]
    return list(Person.people.values())
