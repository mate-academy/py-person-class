class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    list_of_created_people = []
    has_wife = []
    has_husband = []
    counter_for_pairs = 0
    print(people)
    for person in people:
        inst_person = Person(person["name"], person["age"])
        list_of_created_people.append(inst_person)
        if ("wife" in person.keys()):
            if person["wife"]:
                has_wife.append([inst_person, person["wife"]])
                counter_for_pairs += 1
        if ("husband" in person.keys()):
            if person["husband"]:
                has_husband.append([inst_person, person["husband"]])
    while counter_for_pairs > 0:
        print(has_wife)
        print(has_husband)
        husband = has_wife.pop(0)
        for i in range(counter_for_pairs):
            if husband[1] == has_husband[i][0].name:
                wife = has_husband.pop(i)
                husband[0].wife, wife[0].husband = wife[0], husband[0]
                counter_for_pairs -= 1
                break
    return list_of_created_people
