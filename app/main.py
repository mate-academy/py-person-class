class Person:
    people = {}

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        Person.people[self.name] = self

    def wife_add(self, wife) -> None:
        self.wife = wife

    def husband_add(self, husband) -> None:
        self.husband = husband


def create_person_list(people_list: list) -> list:
    people = [person for person in people_list]
    for index in range(len(people)):
        people[index] = Person(people[index]["name"], people[index]["age"])

    for index in range(len(people_list)):
        married_gender = "wife" if "wife" in people_list[index] else "husband"
        for married_with in range(len(people_list)):
            if people_list[index][married_gender] == \
                    people_list[married_with]["name"] \
                    and married_gender == "wife":
                people[index].wife_add(people[married_with])
            if people_list[index][married_gender] == \
                    people_list[married_with]["name"] \
                    and married_gender == "husband":
                people[index].husband_add(people[married_with])

    return people
