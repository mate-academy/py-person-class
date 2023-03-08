class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list[dict[str, any]]) -> list[Person]:
    person_dict = {person["name"]: Person(person["name"],
                                          person["age"]) for person in people}
    for person in people:
        if person.get("wife"):
            person_dict[
                person["name"]].wife = person_dict[person["wife"]]
        if person.get("husband"):
            person_dict[
                person["name"]].husband = person_dict[person["husband"]]
    return list(person_dict.values())
