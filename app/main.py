class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_of_function = [Person(element["name"], element["age"])
                          for element in people
                          ]
    for number in range(len(people)):
        keys_of_people = list(people[number].keys())
        if keys_of_people[2] == "wife" and people[number]["wife"] is not None:
            result_of_function[number].wife \
                = Person.people[people[number]["wife"]]
        if (keys_of_people[2] == "husband"
                and people[number]["husband"] is not None):
            result_of_function[number].husband \
                = Person.people[people[number]["husband"]]
    return result_of_function
