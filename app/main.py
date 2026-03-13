class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    if people == []:
        return []
    people_class_list = []
    for person in people:
        people_class_list.append(Person(person["name"], person["age"]))
    for i in range(len(people)):
        if people[i].get("husband") is not None:
            hsb = Person.people.get(people[i].get("husband"))
            people_class_list[i].husband = hsb
        if people[i].get("wife") is not None:
            wf = Person.people.get(people[i].get("wife"))
            people_class_list[i].wife = wf
    return people_class_list
