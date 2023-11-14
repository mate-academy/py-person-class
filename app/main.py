class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_people = []
    for character in people:
        list_of_people.append(
            Person(
                name=character["name"],
                age=character["age"]
            )
        )
    for index in range(len(list_of_people)):
        if "wife" in people[index]:
            if people[index]["wife"]:
                list_of_people[index].wife = Person.people[
                    people[index]["wife"]
                ]
        if "husband" in people[index]:
            if people[index]["husband"]:
                list_of_people[index].husband = Person.people[
                    people[index]["husband"]
                ]
    return list_of_people
