class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[self.name] = self


def create_person_list(people: list) -> list:
    list_of_people = [Person(person["name"], person["age"])
                      for person in people]
    for one in people:
        for key in one:
            if key == "wife":
                if one["wife"] is not None:
                    Person.people[one["name"]].wife\
                        = Person.people[one["wife"]]
            elif key == "husband":
                if one["husband"] is not None:
                    Person.people[one["name"]].husband\
                        = Person.people[one["husband"]]
    return list_of_people
