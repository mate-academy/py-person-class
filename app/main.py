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
        peoples_dict[f"{name}"] = Person(name, age)

        try:
            wife = people_one["wife"]
            peoples_dict[f"{name}"].wife = wife
        except Exception:
            husband = people_one["husband"]
            peoples_dict[f"{name}"].husband = husband

    for key in list(peoples_dict.keys()):
        if hasattr(peoples_dict[key], "wife"):
            if peoples_dict[key].wife in peoples_dict.keys() \
                    and peoples_dict[key].wife is not None:
                peoples_dict[key].wife = peoples_dict[peoples_dict[key].wife]

        if hasattr(peoples_dict[key], "husband"):
            if peoples_dict[key].husband in peoples_dict.keys() \
                    and peoples_dict[key].husband is not None:
                peoples_dict[key].husband = \
                    peoples_dict[peoples_dict[key].husband]

    res_list = list(peoples_dict.values())
    for people in res_list:
        if hasattr(people, "wife") and people.wife is None:
            delattr(people, 'wife')
        elif hasattr(people, "husband") and people.husband is None:
            delattr(people, 'husband')

    return res_list
