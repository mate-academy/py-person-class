class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people.setdefault(self.name, self)

    def __str__(self) -> str:
        return f"{self.name}, {self.age}"


def create_person_list(people: list) -> list:
    list_instances = []
    for i in range(len(people)):
        list_instances.append(Person(people[i]["name"], people[i]["age"]))
    for first_person in range(len(people)):
        if "wife" in people[first_person].keys():
            for second_person in range(len(people)):
                if people[first_person]["wife"] == \
                        people[second_person]["name"]:
                    list_instances[first_person].wife = \
                        list_instances[second_person]
        if "husband" in people[first_person].keys():
            for second_person in range(len(people)):
                if people[first_person]["husband"] == \
                        people[second_person]["name"]:
                    list_instances[first_person].husband = \
                        list_instances[second_person]
    return list_instances
