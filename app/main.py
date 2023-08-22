class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    people_objs = []

    for person in people:
        new_person = Person(person["name"], person["age"])
        wife, husband = person.get("wife"), person.get("husband")

        if wife:
            new_person.wife = wife

        if husband:
            new_person.husband = husband

        people_objs.append(new_person)

    #  marry persons
    for person in people_objs:
        if hasattr(person, "wife"):
            person.wife = Person.people[person.wife]

        if hasattr(person, "husband"):
            person.husband = Person.people[person.husband]

    return people_objs
