class Person:
    people = {}

    def __init__(self, name: str, age: int,) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_lst: list) -> list:

    friends = [
        Person(
            person_dic["name"], person_dic["age"]
        )
        for person_dic in people_lst
    ]
    # filter by woman and husband and his existing

    for person in people_lst:
        if person.get("husband"):
            Person.people[person["name"]].husband = (
                Person.people.get(person["husband"])
            )
        if person.get("wife"):
            Person.people[person["name"]].wife = (
                Person.people.get(person["wife"])
            )

    return friends
