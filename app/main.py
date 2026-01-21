class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()
    [Person(person_data["name"], person_data["age"])
        for person_data in people]
    for person_data in people:
        person = Person.people[person_data["name"]]
        if (person_data.get("wife") and person_data["wife"]
                in Person.people):
            person.wife = Person.people[person_data["wife"]]
        if (person_data.get("husband") and person_data["husband"]
                in Person.people):
            person.husband = Person.people[person_data["husband"]]

    return [Person.people[person_data["name"]] for person_data in people]
