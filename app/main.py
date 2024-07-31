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
    for num, person in enumerate(people_list):
        if "wife" in people[num] and people[num]["wife"]:
            person.wife = people[num]["wife"]
            for person_wife in people_list:
                if person_wife.name == person.wife:
                    person.wife = person_wife
        if "husband" in people[num] and people[num]["husband"]:
            person.husband = people[num]["husband"]
            for person_husband in people_list:
                if person_husband.name == person.husband:
                    person.husband = person_husband

    return people_list
