class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    res_list = []

    for dic in people:
        if None in dic.values():
            res_list.append(Person(dic["name"], dic["age"]))
        elif "wife" in dic.keys():
            person = Person(dic["name"], dic["age"])
            person.wife = dic["wife"]
            res_list.append(person)
        elif "husband" in dic.keys():
            person = Person(dic["name"], dic["age"])
            person.husband = dic["husband"]
            res_list.append(person)

    for person_obj in res_list:
        temp_dic = vars(person_obj)
        if "wife" in temp_dic.keys():
            name_wife = temp_dic["wife"]
            person_obj.wife = Person.people[name_wife]
        elif "husband" in temp_dic.keys():
            name_husband = temp_dic["husband"]
            person_obj.husband = Person.people[name_husband]

    return res_list
