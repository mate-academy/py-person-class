class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:

        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:

    people_dict = {}

    for i in people:
        name = i["name"]
        age = i["age"]
        person = Person(name, age)
        people_dict[name] = person

    for i in people:
        name = i["name"]
        if "wife" in i and i["wife"]:
            wife_name = i["wife"]
            wife = people_dict[wife_name]

            if wife is not None:
                people_dict[name].wife = wife

        elif "husband" in i and i["husband"]:
            husband_name = i["husband"]
            people_dict[name].husband = people_dict[husband_name]

    return list(people_dict.values())
