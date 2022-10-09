class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.__class__.people.update({self.name: self})


def create_person_list(people: list) -> list:
    person_list = []
    for person in people:
        person_list.append(Person(person["name"], person["age"]))
    for i in range(len(people)):
        for key, value in people[i].items():
            if key == "wife":
                if value is not None:
                    Person.people[
                        people[i]["name"]].wife = Person.people[value]
                    Person.people[
                        people[i]["name"]].wife.husband = Person.people[
                        people[i]["name"]]
    return person_list
