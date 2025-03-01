import pickle

def create_binary_file_with_marks(filename):
    with open(filename, 'wb') as file:
        while True:
            roll_no = input("Enter Roll No (or 'exit' to stop): ")
            if roll_no.lower() == 'exit':
                break
            name = input("Enter Name: ")
            marks = float(input("Enter Marks: "))
            pickle.dump((roll_no, name, marks), file)

def update_marks(filename, roll_no, new_marks):
    records = []
    found = False
    with open(filename, 'rb') as file:
        while True:
            try:
                record = pickle.load(file)
                if record[0] == roll_no:
                    record = (record[0], record[1], new_marks)
                    found = True
                records.append(record)
            except EOFError:
                break

    with open(filename, 'wb') as file:
        for record in records:
            pickle.dump(record, file)

    return found

filename = 'students_with_marks.dat'
create_binary_file_with_marks(filename)
roll_no_to_update = input("Enter Roll No to update marks: ")
new_marks = float(input("Enter new marks: "))
if update_marks(filename, roll_no_to_update, new_marks):
    print("Marks updated successfully.")
else:
    print("Roll No not found.")
