class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    new_object_person = [Person(person["name"], person["age"])
                         for person in people]

    for person in people:
        current_person = Person.people[person["name"]]
        wife = person.get("wife")
        if wife:
            current_person.wife = Person.people[wife]

        husband = person.get("husband")
        if husband:
            current_person.husband = Person.people[husband]
    return new_object_person
