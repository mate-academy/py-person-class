class Person:
    people = {}

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    peoples_dict = {}
    for people_one in people:
        name = people_one["name"]
        age = people_one["age"]
        peoples_dict[name] = Person(name, age)

    for people_one in people:
        print(people_one)

        if "wife" in people_one.keys() and people_one["wife"] is not None:
            peoples_dict[people_one["name"]].wife = people_one["wife"]

            if people_one["wife"] in peoples_dict.keys():
                peoples_dict[people_one["name"]].wife = \
                    peoples_dict[people_one["wife"]]

        if "husband" in people_one.keys() and \
                people_one["husband"] is not None:
            peoples_dict[people_one["name"]].husband = people_one["husband"]

            if people_one["husband"] in peoples_dict.keys():
                peoples_dict[people_one["name"]].husband = \
                    peoples_dict[people_one["husband"]]

    return [res_people for res_people in peoples_dict.values()]
