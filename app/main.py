class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = []

    for person in people:
        person_instance = None

        if person["name"] in Person.people.keys():
            person_instance = Person.people[person["name"]]
        else:
            person_instance = Person(person["name"], person["age"])

        persons_list.append(person_instance)

        if person.get("wife"):
            if person["wife"] in Person.people.keys():
                person_instance.wife = Person.people[person["wife"]]
            else:
                wife = [
                    human
                    for human in people
                    if human["name"] == person["wife"]
                ][0]
                person_instance.wife = Person(wife["name"], wife["age"])

        if person.get("husband"):
            if person["husband"] in Person.people.keys():
                person_instance.husband = Person.people[person["husband"]]
            else:
                husband = [
                    human
                    for human in people
                    if human["name"] == person["husband"]
                ][0]
                person_instance.husband = Person(
                    husband["name"], husband["age"]
                )

    return persons_list
