class Person:
    people = {}

    def __init__(self,
                 name: str,
                 age: str) -> None:
        self.name = name
        self.age = age
        self.people[self.name] = self


def create_person_list(p_list: list) -> list:
    return_list = []

    for i, prs in enumerate(p_list):
        return_list.append(Person(prs["name"], prs["age"]))
        if "wife" in prs and prs["wife"] is not None:
            return_list[i].wife = prs["wife"]
        if "husband" in prs and prs["husband"] is not None:
            return_list[i].husband = prs["husband"]

    for prs_name in return_list:
        for maried_prs in return_list:
            if "wife" in maried_prs.__dict__:
                if maried_prs.wife == prs_name.name:
                    maried_prs.wife = prs_name
                    prs_name.husband = maried_prs

    return return_list
