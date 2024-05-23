class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = [Person(person_data["name"], person_data["age"])
                      for person_data in people]

    for person_data in people:
        name = person_data["name"]
        person = Person.people[name]
        spouse = person_data.get("wife") or person_data.get("husband")
        if spouse:
            spouse = Person.people[spouse]
            if "wife" in person_data:
                person.wife = spouse
            else:
                person.husband = spouse
    return list_of_people
