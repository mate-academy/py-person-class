class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = list()

    for person_info in people:
        person_entry = Person(name=person_info["name"], age=person_info["age"])
        people_list.append(person_entry)

    for person in people:
        if person.get("husband"):
            Person.people[person["name"]].husband = Person.people[
                person["husband"]]
        elif person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]

    return people_list
