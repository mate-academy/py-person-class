class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    result_list = [Person(people_it["name"],
                          people_it["age"])
                   for people_it in people]

    for item in people:
        person = Person.people[item["name"]]
        if "wife" in item and item["wife"] is not None:
            person.wife = Person.people[item["wife"]]
        if "husband" in item and item["husband"] is not None:
            person.husband = Person.people[item["husband"]]
    return result_list
