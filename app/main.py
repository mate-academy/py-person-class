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
    ind_val = 0  # for iteration inside for loop
    for values in people:
        keys_of_people = list(values.keys())
        if keys_of_people[2] == "wife" and values["wife"] is not None:
            result_of_function[ind_val].wife = Person.people[values["wife"]]
        if keys_of_people[2] == "husband" and values["husband"] is not None:
            result_of_function[ind_val].husband \
                = Person.people[values["husband"]]
        ind_val += 1
    return result_of_function
