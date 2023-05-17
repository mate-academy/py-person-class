class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = [Person(current_person["name"], current_person["age"])
                   for current_person in people]

    for i in range(len(person_list)):
        if "wife" in people[i] and people[i]["wife"] is not None:
            name_of_the_wife = people[i]["wife"]
            person_list[i].wife = Person.people[name_of_the_wife]
        elif "husband" in people[i] and people[i]["husband"] is not None:
            name_of_the_husband = people[i]["husband"]
            person_list[i].husband = Person.people[name_of_the_husband]

    return person_list
