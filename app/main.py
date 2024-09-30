class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for human in people:
        each_person = Person(human["name"], human["age"])
        person_list.append(each_person)
        for key in human.keys():
            if key == "wife" and human["wife"] is not None:
                each_person.wife = human["wife"]
            elif key == "husband" and human["husband"] is not None:
                each_person.husband = human["husband"]
            else:
                continue
    for each_pep in person_list:
        for key, value in Person.people.items():
            if hasattr(each_pep, "wife") and key == each_pep.wife:
                each_pep.wife = value
            elif hasattr(each_pep, "husband") and key == each_pep.husband:
                each_pep.husband = value
    return person_list
