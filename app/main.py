class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    result = [Person(person_dic["name"], person_dic["age"])
              for person_dic in people]

    for person_dic in people:
        name = person_dic["name"]

        if person_dic.get("wife"):
            Person.people[name].wife = Person.people[person_dic["wife"]]

        if person_dic.get("husband"):
            Person.people[name].husband = Person.people[person_dic["husband"]]

    return result
