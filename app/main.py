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
    print("\n")
    print("People:", people)

    for person in people:
        # out.append(Person(person["name"], person["age"], person["wife"], person["husband"]))

        new = Person(name=person["name"], age=person["age"])
        out.append(new)
        # new = Person(name=person["name"], age=person["age"], wife=person["wife"], husband=person["husband"])
        # print(new.name)
    # for i in out:
    #     # print(i)
    #     print(i.name, i.age, i.wife, i.husband)
    #     for j in people:
    #         print(i.name)
    #         if ("wife" in j) and (j["wife"] == i.name) and (j["wife"] is not None):
    #             i.wife = i
    #             print("!!!! wife ", i.name, j["wife"], i.wife.name)
    #         if ("husband" in j) and (j["husband"] == i.name) and (j["husband"] is not None):
    #             i.husband = i
    #             print("!!!! husband", i.name, j["husband"], i.husband.name)
    vsi = Person.people
    print("VSE:", vsi)

    # for persona in out:
    for n, j in enumerate(people):
        print(j, n)
        if ("wife" in j) and (j["wife"] is not None):
            print("Zena:", j["wife"], n, vsi[j["wife"]] )
            out[n].wife = vsi[j["wife"]]

    for n, j in enumerate(people):
        print(j, n)
        if ("husband" in j) and (j["husband"] is not None):
            print("Zena:", j["husband"], n, vsi[j["husband"]])
            out[n].husband = vsi[j["husband"]]

    print("out", out)








        #             i.wife = i
        #             print("!!!! wife ", i.name, j["wife"], i.wife.name)








    # for person in people:
    #     for data in out:
    #         if person["wife"] == data.name:
    #             data.wife = data
    #         if person["husband"] == data.name:
    #             data.husband = data

    return out










