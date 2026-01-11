class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []

    for person in people:
        people_list.append(Person(name=person["name"], age=person["age"]))

    for i, person in enumerate(people):
        current = people_list[i]
        if person.get("wife"):
            for idx, spouse in enumerate(people):
                if person.get("wife") and spouse["name"] == person["wife"]:
                    current.wife = people_list[idx]

        elif person.get("husband"):
            for idx, spouse in enumerate(people):
                if person.get("husband") and (
                    spouse["name"] == person["husband"]
                ):
                    current.husband = people_list[idx]

    return people_list
