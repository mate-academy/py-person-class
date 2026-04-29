class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    Person.people.clear()

    person_list = [Person(person["name"], person["age"]) for person in people]

    for person_dict, person_obj in zip(people, person_list):
        wife = person_dict.get("wife")
        husband = person_dict.get("husband")

        if wife:
            Person.people[wife].husband = person_obj
            person_obj.wife = Person.people[wife]
        if husband:
            Person.people[husband].wife = person_obj
            person_obj.husband = Person.people[husband]

    return person_list
