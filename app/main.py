class Person:
    # write your code here
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.wife = None
        self.husband = None
        self.people[self.name] = self


def create_person_list(people: list) -> list:
    out = []

    for person in people:
        # out.append(Person(person["name"], person["age"], person["wife"], person["husband"]))
        print(person["name"])
        new = Person(name=person["name"], age=person["age"])
        out.append(new)
        # new = Person(name=person["name"], age=person["age"], wife=person["wife"], husband=person["husband"])
        # print(new.name)
    for i in out:
        print(i)
        print(i.name, i.age, i.wife, i.husband)
        for j in people:
        #     # if i.name == person["wife"]:
            if ("wife" in j) and (j["wife"] == i.name) and (j["wife"] is not None):
                i.wife = i
                print("!!!! ", i.name, j["wife"], i.wife.name)
            if ("husband" in j) and (j["husband"] == i.name) and (j["husband"] is not None):
                i.husband = i
                print("!!!! ", i.name, j["husband"], i.husband.name)

    # for person in people:
    #     for data in out:
    #         if person["wife"] == data.name:
    #             data.wife = data
    #         if person["husband"] == data.name:
    #             data.husband = data
    return out










