class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self



def create_person_list(people: list) -> list:

    list_of_persons = []
    for item in people:
        list_of_persons.append(Person(name=item["name"], age=item["age"]))

    for item in people:
        if "wife" in item.keys() and item["wife"] is not None:
            wife_to_insert = Person.people[item["wife"]]
            Person.people[item["name"]].wife = wife_to_insert

        if "husband" in item.keys() and item["husband"] is not None:
            husband_to_insert = Person.people[item["husband"]]
            Person.people[item["name"]].husband = husband_to_insert

    return list_of_persons
