class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_peoples = []
    for i in people:
        keys = [j for j in i]
        list_of_peoples.append(Person(i["name"], i["age"]))

        if i[keys[2]] is not None:
            if keys[2] == "husband":
                list_of_peoples[-1].husband = i[keys[2]]
            else:
                list_of_peoples[-1].wife = i[keys[2]]

    for i in list_of_peoples:
        keys = [j for j in i.__dict__]
        if len(keys) > 2:
            for people in list_of_peoples:
                if keys[2] == "wife":
                    if i.wife == people.name:
                        i.wife = people
                else:
                    if i.husband == people.name:
                        i.husband = people

    return list_of_peoples
