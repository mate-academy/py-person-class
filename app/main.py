class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_people = [Person(person["name"], person["age"])
                      for person in people]
    for human in people:
        if human.get("wife"):
            husband = Person.people[human["name"]]
            husband.wife = Person.people[human["wife"]]
        if human.get("husband"):
            wife = Person.people[human["name"]]
            wife.husband = Person.people[human["husband"]]
    return list_of_people
