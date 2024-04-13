class Person:
    people = {}

    def __init__(self, name: str, age: int,) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people_lst: list) -> list:

    friends = [Person(i["name"], i["age"]) for i in people_lst]
    # filter by woman and husband and his existing
    for person in [
        woman for woman in people_lst if "husband" in woman.keys()
                                         and woman["husband"]
    ]:
        if person["husband"]:
            Person.people[person["name"]].husband = (
                Person.people.get(person["husband"])
            )
    # filter by man and wife and her existing
    for person in [
        man for man in people_lst if "wife" in man.keys()
    ]:
        if person["wife"]:
            Person.people[person["name"]].wife = (
                Person.people.get(person["wife"])
            )
    return friends
