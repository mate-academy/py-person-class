

class Person:

    people = {}

    def __init__(self, name: str, age: int):

        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for human in people:
        person_list.append(Person(human["name"], human["age"]))
    for human in people:
        if human.get("wife") is not None:
<<<<<<< HEAD
            husband = Person.people[human["name"]]
            husband.wife = Person.people[human["wife"]]
        elif human.get("husband") is not None:
            wife = Person.people[human["name"]]
            wife.husband = Person.people[human["husband"]]
=======
            Person.people[human["name"]].wife = \
                Person.people[human["wife"]]
        elif human.get("husband") is not None:
            Person.people[human["name"]].husband = \
                Person.people[human["husband"]]
>>>>>>> 451bc70daec1055bf9846a28fbd78e754b6c2cb1
    return person_list
