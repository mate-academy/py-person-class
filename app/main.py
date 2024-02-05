class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [
        Person(name=person.get("name"), age=person.get("age"))
        for person in people
    ]
    for person in people:
        prs_name = person.get("name")
        prs_wife = person.get("wife")
        prs_husband = person.get("husband")
        if prs_wife:
            Person.people[prs_name].wife = Person.people.get(prs_wife)
        elif prs_husband:
            Person.people[prs_name].husband = Person.people.get(prs_husband)
    return people_list
