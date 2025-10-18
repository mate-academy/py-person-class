class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_person = [Person(person["name"], person["age"]) for person in people]
    for i in range(len(people)):
        if "wife" in people[i]:
            if people[i]["wife"]:
                list_person[i].wife = people[i]["wife"]
                for jot in range(len(people)):
                    if list_person[i].wife == list_person[jot].name:
                        list_person[i].wife = list_person[jot]
        elif "husband" in people[i]:
            list_person[i].husband = people[i]["husband"]
            for jot in range(len(people)):
                if list_person[i].husband == list_person[jot].name:
                    list_person[i].husband = list_person[jot]
    return list_person
