class Person:
    people = {}

    def __init__(self,
                 name: str,
                 age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    ls_of_friends = [Person(person["name"], person["age"])for person in people]
    for person in people:
        wife = person.get("wife")
        husband = person.get("husband")
        if wife:
            Person.people[person.get("name")].wife = Person.people[wife]
        if husband:
            Person.people[person.get("name")].husband = Person.people[husband]

    return ls_of_friends
