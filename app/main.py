class Person:
    # Class variable to store all people instances
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        # Add the current person instance to the people dictionary
        Person.people[name] = self


def create_person_list(people: list) -> list:
    # List to store person instances
    people_by_name = []

    # Create person instances from the list of dictionaries
    for person in people:
        person_by_name = Person(person["name"], person["age"])
        people_by_name.append(person_by_name)

    # Assign spouses to each person
    for person in people:
        if person.get("wife"):
            Person.people[person["name"]].wife = Person.people[person["wife"]]
        if person.get("husband"):
            Person.people[person["name"]].husband = Person.people[
                person["husband"]
            ]

    return people_by_name
