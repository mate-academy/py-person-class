class Person:
    people = dict()

    def __init__(self, name: str, age: int) -> object:
        self.name = name
        self.age = age
        Person.people[name] = self

    def __str__(self) -> str:
        ans = "name: " + self.name + "  age: " + str(self.age)
        if hasattr(self, "wife"):
            ans += "  wife: " + self.wife.name
        if hasattr(self, "husband"):
            ans += "  husband: " + self.husband.name
        return ans


def create_person_list(people1: list) -> list:
    Person.people.clear()
    ans = []
    for p1 in people1:
        person = Person(p1["name"], p1["age"])
        ans.append(person)

    for p1 in people1:
        spouse_name = None
        key = ""
        if "wife" in p1:
            key = "wife"
            spouse_name = p1["wife"]
        if "husband" in p1:
            key = "husband"
            spouse_name = p1["husband"]

        if spouse_name is not None:
            name = p1["name"]
            person = Person.people[name]
            if key == "wife":
                person.wife = Person.people[spouse_name]
            if key == "husband":
                person.husband = Person.people[spouse_name]

    return ans
