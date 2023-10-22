class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    friends = [Person(someone["name"], someone["age"]) for someone in people]
    for friend in friends:
        for person in people:
            if "wife" in person \
                    and person["wife"] is not None \
                    and friend.name == person["name"]:
                friend.wife = Person.people[person["wife"]]
            elif "husband" in person and person["husband"] is not None:
                friend.husband = Person.people[person["husband"]]
    return friends
