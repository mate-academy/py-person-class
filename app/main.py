class Person:
    people = {}


    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[name] = self

    # def __repr__(self) -> str:
    #     return f"<Person object, {self.__dict__}>"


def create_person_list(people: list) -> list:
    name_list = []
    final_list = []
    for person in people:
        final_list.append(Person(
            name=person.get("name"),
            age=person.get("age")
        ))
        name_list.append(person.get("name"))

    for human in people:
        fiance = list(human.keys())[-1]
        if human.get(fiance) is not None:
            if fiance == "wife":
                final_list[name_list.index(human.get("name"))].wife = final_list[name_list.index(human.get(fiance))]
            elif fiance == "husband":
                final_list[name_list.index(human.get("name"))].husband = final_list[name_list.index(human.get(fiance))]
    return final_list
