class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    # add people to list
    for dict_of_person in people:
        new_person = Person(dict_of_person["name"], dict_of_person["age"])
        person_list.append(new_person)
    # add attributes to each person
    for index1 in range(len(person_list)):
        if "wife" in people[index1]:
            if people[index1]["wife"] is not None:
                for index2 in range(len(people)):
                    if people[index1]["wife"] == people[index2]["name"]:
                        person_list[index1].wife = person_list[index2]

        elif "husband" in people[index1]:
            if people[index1]["husband"] is not None:
                for index2 in range(len(people)):
                    if people[index1]["husband"] == people[index2]["name"]:
                        person_list[index1].husband = person_list[index2]
    return person_list
