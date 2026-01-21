class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    friends = [Person(friend["name"], friend["age"]) for friend in people]

    for person_dict in people:
        instance_person = Person.people[person_dict["name"]]
        if person_dict.get("wife"):
            instance_person.wife = Person.people.get(person_dict["wife"])
        if person_dict.get("husband"):
            instance_person.husband = Person.people.get(person_dict["husband"])

    return friends
