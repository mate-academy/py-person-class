class Person:
    people = {}

    def __init__(self, name: str, age: str) -> None:
        self.name = name
        self.age = age
        self.people.update({name: self})


def create_person_list(people: list) -> list:
    people_list = []
    for person_info in people:
        person = Person(name=person_info["name"], age=person_info["age"])
        people_list.append(person)

    for i in range(len(people)):
        if people[i].get("wife"):
            people_list[i].wife = Person.people.get(people[i].get("wife"))
        elif people[i].get("husband"):
            people_list[i].husband = (
                Person.people.get(people[i].get("husband")))

    return people_list
