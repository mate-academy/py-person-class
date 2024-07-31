class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = [
        Person(person["name"], person["age"])
        for person in people
    ]
    people_dict = {
        person.name: person
        for person in people_list
    }
    for num, person in enumerate(people_list):
        if people[num].get("wife"):
            person_wife = people[num]["wife"]
            person.wife = people_dict[person_wife]
        if people[num].get("husband"):
            person_husband = people[num]["husband"]
            person.husband = people_dict[person_husband]
    return people_list
