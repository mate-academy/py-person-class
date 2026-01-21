class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    friends = [Person(person["name"], person["age"]) for person in people]
    for friend in friends:
        person = [dct for dct in people if dct["name"] == friend.name][0]
        if "husband" in person:
            partner = "husband", person["husband"]
        else:
            partner = "wife", person["wife"]
        if partner[1] is not None:
            setattr(friend, partner[0], Person.people[partner[1]])
    return friends
