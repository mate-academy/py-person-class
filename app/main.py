class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_of_people = [
        Person(name=person["name"],
               age=person["age"])
        for person in people
        ]
    for person, person_dict in zip(persons_of_people, people):
        wife_name = person_dict.get("wife")
        husband_name = person_dict.get("husband")
        if wife_name:
            person.wife = Person.people.get(wife_name)
        if husband_name:
            person.husband = Person.people.get(husband_name)

    return persons_of_people
