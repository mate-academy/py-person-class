class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.setdefault(self.name, self)


def create_person_list(people: list) -> list:
    links_of_instances = [
        Person(people[person]["name"], people[person]["age"])
        for person in range(len(people))]

    for waifu in range(len(people)):
        if "wife" in people[waifu].keys():
            for crash in range(len(people)):
                if people[waifu]["wife"] == \
                        people[crash]["name"]:
                    links_of_instances[waifu].wife = \
                        links_of_instances[crash]
        if "husband" in people[waifu].keys():
            for crash in range(len(people)):
                if people[waifu]["husband"] == \
                        people[crash]["name"]:
                    links_of_instances[waifu].husband = \
                        links_of_instances[crash]

    return links_of_instances
