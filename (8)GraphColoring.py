slots = ["9.00", "11.00", "1.00", "3.00"]
subjects = ["MATHS", "OS", "ARM", "DAA", "BIO"]

enrolled = {}
enrolled["MATHS"] = ["ARM", "BIO", "DAA", "OS"]
enrolled["OS"] = ["ARM", "BIO", "DAA", "MATHS"]
enrolled["ARM"] = ["OS", "BIO", "DAA", "MATHS"]
enrolled["DAA"] = ["ARM", "BIO", "OS", "MATHS"]
enrolled["BIO"] = ["ARM", "OS", "DAA", "MATHS"]

scheduled_time_slots = {}


def promising(subject, slot):
    for students in enrolled.get(subject):
        allocated_slots = scheduled_time_slots.get(students)
        if allocated_slots == slot:
            return False
    return True


def get_time_slots(subject):
    for slot in slots:
        if promising(subject, slot):
            return slot


def main():
    for subject in subjects:
        scheduled_time_slots[subject] = get_time_slots(subject)
    print(scheduled_time_slots)


main()
