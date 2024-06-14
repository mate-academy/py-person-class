class Person:

    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list[dict]) -> list[Person]:
    lst = []
    with_wifes = []
    with_husbands = []

    for dic in people:
        if "wife" in dic and dic["wife"]:
            man = Person(dic["name"], dic["age"])
            man.wife = dic["wife"]
            with_wifes.append(man)
            lst.append(man)
        elif "husband" in dic and dic["husband"]:
            man = Person(dic["name"], dic["age"])
            man.wife = dic["husband"]
            with_husbands.append(man)
            lst.append(man)
        else:
            lst.append(Person(dic["name"], dic["age"]))
    for man in with_wifes:
        for woman in with_husbands:
            if man.wife == woman.name:
                man.wife = woman
                woman.husband = man
    return lst
