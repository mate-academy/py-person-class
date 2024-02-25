class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        self.people[name] = self


def create_person_list(humans: list) -> list:
    persons_list = [Person(man["name"], man["age"]) for man in humans]
    for num in range(len(humans)):
        if humans[num].get("husband"):
            for man in persons_list:
                if man.name == humans[num].get("husband"):
                    persons_list[num].husband = man
        elif humans[num].get("wife"):
            for woman in persons_list:
                if woman.name == humans[num].get("wife"):
                    persons_list[num].wife = woman
    return persons_list
