class Person:

    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:

    friends = [Person(person['name'], person['age']) for person in people]

    for one_friend in people:
        if one_friend.get('wife') is not None:
            Person.people[one_friend['name']].wife = Person.people[one_friend['wife']]
        if one_friend.get('husband') is not None:
            Person.people[one_friend['name']].husband = Person.people[one_friend['husband']]
    return friends
