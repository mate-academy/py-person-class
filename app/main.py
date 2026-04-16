class Person:
    people = {}

    def __init__(self, name : str, age : int) -> None :
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    persons_list = []

    for index, person in enumerate(people):
        persons_list.append(Person(person["name"], person["age"]))

    for index, person in enumerate(people):
        status = list(person.keys())[-1]
        if status in person is not None:
            if status == "wife":
                name_wife = person["wife"]
                for i in range(len(persons_list)):
                    if persons_list[i].name == name_wife:
                        persons_list[index].wife = persons_list[i]
            else:
                name_husband = person["husband"]
                for i in range(len(persons_list)):
                    if persons_list[i].name == name_husband:
                        persons_list[index].husband = persons_list[i]

    return persons_list
