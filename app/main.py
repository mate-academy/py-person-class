class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    people_list = []
    for human in people:
        people_list.append(Person(human["name"], human["age"]))

    for man in people:
        for key in man.keys():
            if key == "wife":
                for i in range(len(people_list)):
                    if people_list[i].name == man["wife"]:
                        for j in range(len(people_list)):
                            if people_list[j].name == man["name"]:
                                people_list[j].wife = people_list[i]

            elif key == "husband":
                for i in range(len(people_list)):
                    if people_list[i].name == man["husband"]:
                        for j in range(len(people_list)):
                            if people_list[j].name == man["name"]:
                                people_list[j].husband = people_list[i]

    return people_list
