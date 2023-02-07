class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

        Person.people[name] = self


def create_person_list(people: list) -> list:
    result_list = []
    for human_being in people:
        adding_person = Person(human_being["name"], human_being["age"])
        result_list.append(adding_person)

    for human_being in people:

        getting_wife = human_being.get("wife")
        getting_husband = human_being.get("husband")

        if getting_wife is not None:
            Person.people[human_being["name"]].wife = Person.people[
                                                            human_being["wife"]
                                                      ]
        if getting_husband is not None:
            Person.people[human_being["name"]].husband = Person.people[
                                                                human_being["husband"]
                                                        ]

    return result_list
