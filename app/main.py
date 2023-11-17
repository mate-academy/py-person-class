class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    nameparts = []
    for person in people:
        person1 = list(person.values())
        person2 = list(person.keys())
        name = person1[0]
        age = person1[1]

        keylist = person2[2]
        secondpart = person1[2]

        nameparts.append(secondpart)

        person_list.append(Person(name, age))

    super_j = 0
    for name in nameparts:
        if name is None:
            pass
        else:
            for i in range(len(person_list)):
                if person_list[i].name == name:
                    if keylist[i] == "wife":
                        person_list[super_j].husband = person_list[i]
                    else:
                        person_list[super_j].wife = person_list[i]
        super_j += 1

    return person_list
