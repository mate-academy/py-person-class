class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_people = []

    for person_data in people:
        name = person_data["name"]
        age = person_data["age"]
        new_person = Person(name, age)
        list_of_people.append(new_person)

        if "wife" in person_data and person_data["wife"] in Person.people:
            new_person.wife = Person.people[person_data["wife"]]
            Person.people[person_data["wife"]].husband = new_person
        elif "husband" in person_data and \
             person_data["husband"] in Person.people:
            new_person.husband = Person.people[person_data["husband"]]
            Person.people[person_data["husband"]].wife = new_person

    return list_of_people
