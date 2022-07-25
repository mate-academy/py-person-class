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
            try:
                peoples_dict[people_one["name"]].wife = \
                    peoples_dict[people_one["wife"]]
            except Exception:
                pass

        if "husband" in people_one.keys() and \
                people_one["husband"] is not None:
            peoples_dict[people_one["name"]].husband = people_one["husband"]
            try:
                peoples_dict[people_one["name"]].husband = \
                    peoples_dict[people_one["husband"]]
            except Exception:
                pass

    return [res_people for res_people in peoples_dict.values()]
