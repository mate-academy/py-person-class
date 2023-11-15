class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_people = [
        Person(name=character["name"], age=character["age"])
        for character in people
    ]
    for index in range(len(list_of_people)):
        wife_name = people[index].get("wife")

        husband_name = people[index].get("husband")

        if wife_name:
            list_of_people[index].wife = Person.people[
                people[index]["wife"]
            ]

        if husband_name:
            list_of_people[index].husband = Person.people[
                people[index]["husband"]
            ]

    return list_of_people
