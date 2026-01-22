class Person:
    people = {}

    def __init__(self,
                 name: str,
                 age: int,
                 ) -> None:
        self.name = name
        self.age = age
        Person.people.update({self.name: self})


def create_person_list(people: list) -> list:
    person_list = [Person(person["name"], person["age"])
                   for person in people]
    for index, person in enumerate(people):
        for key, value in person.items():
            for key_people, value_people in Person.people.items():
                if key == "wife" and value == key_people:
                    person_list[index].wife = value_people
                elif key == "husband" and value == key_people:
                    person_list[index].husband = value_people

    return person_list
