class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for person in people:
        person_temp = Person(person["name"], person["age"])
        if person.get("wife"):
            wife = Person.people.get(person["wife"])
            if wife:
                person_temp.wife = wife
                wife.husband = person_temp

        people_list.append(person_temp)

    return people_list
