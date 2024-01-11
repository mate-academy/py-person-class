class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people.update({name: self})


def create_person_list(people: list) -> list:
    persons_of_people = [
        Person(name=person["name"],
               age=person["age"])
        for person in people
    ]
    for i in range(len(persons_of_people)):
        person = persons_of_people[i]
        person_dict = people[i]
        if "wife" in person_dict and person_dict["wife"] is not None:
            person.wife = Person.people[person_dict["wife"]]
        if "husband" in person_dict and person_dict["husband"] is not None:
            person.husband = Person.people[person_dict["husband"]]
    return persons_of_people
