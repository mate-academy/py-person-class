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
    for key, value in Person.people.items():
        for person in people:
            if key == person["name"]\
                    and "wife" in person.keys()\
                    and person["wife"]:
                value.wife = Person.people[person["wife"]]
            if key == person["name"]\
                    and "husband" in person.keys()\
                    and person["husband"]:
                value.husband = Person.people[person["husband"]]

    return ls_of_friends
