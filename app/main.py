class Person:
    people_dict = {}
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        Person.people_dict[name] = self


def create_person_list(people: list) -> list:
    people_list = []

    for person in people:
        person_in_list = Person(person["name"], person["age"])
        people_list.append(person_in_list)
    for person in people:
        wife_name = person.get("wife")
        husband_name = person.get("husband")
        if wife_name:
            Person.people_dict[person["name"]].wife = Person.people_dict[person["wife"]]
        elif husband_name:
            Person.people_dict[person["name"]].husband = Person.people_dict[person["husband"]]

    return people_list
