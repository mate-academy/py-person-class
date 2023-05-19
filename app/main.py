class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_people = [Person(person["name"], person["age"])
                      for person in people]
    for person in people:
        wife = person.get("wife")
        husband = person.get("husband")
        if wife is not None:
            Person.people[person["name"]].wife = Person.people[wife]
        if husband is not None:
            Person.people[person["name"]].husband = Person.people[husband]
    return list_of_people
