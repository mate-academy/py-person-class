class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age


def create_person_list(people: list) -> list:
    person_list = []

    for human in people:
        new_person = Person(name=human["name"], age=human["age"])

        Person.people.update({human["name"]: new_person})
        person_list.append(new_person)

    filt_wife = [
        human for human in people if "wife" in human and human["wife"]
    ]
    filt_husband = [
        human for human in people if "husband" in human and human["husband"]
    ]

    for wife in filt_wife:
        for husband in filt_husband:

            filt_wife_person = [
                instance for instance in Person.people.values()
                if instance.name == wife["wife"]
            ]
            filt_husband_person = [
                instance for instance in Person.people.values()
                if instance.name == husband["husband"]
            ]

            filt_husband_person[0].wife = filt_wife_person[0] \
                if filt_wife_person[0] \
                else wife["wife"]

            filt_wife_person[0].husband = filt_husband_person[0] \
                if filt_husband_person[0] \
                else husband["husband"]

    return person_list
