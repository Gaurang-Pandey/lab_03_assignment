class Process:
    def __init__(self, id, name, time, priority):
        self.id = id
        self.name = name
        self.time = time
        self.priority = priority

    def display(self):
        print(f"{self.id}\t{self.name}\t{self.time}\t{self.priority}")

class ProcessTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sorter(self, key_func):
        n = len(self.processes)
        for i in range(n - 1):
            for j in range(0, n - i - 1):
                if key_func(self.processes[j]) > key_func(self.processes[j + 1]):
                    self.processes[j], self.processes[j + 1] = self.processes[j + 1], self.processes[j]

    def display_table(self):
        for process in self.processes:
            process.display()

def main():
    process_table = ProcessTable()

    # Sample data
    process_table.add_process(Process("P1", "VSCode", 100, "MID"))
    process_table.add_process(Process("P23", "Eclipse", 234, "MID"))
    process_table.add_process(Process("P93", "Chrome", 189, "High"))
    process_table.add_process(Process("P42", "JDK", 9, "High"))
    process_table.add_process(Process("P9", "CMD", 7, "High"))
    process_table.add_process(Process("P87", "NotePad", 23, "Low"))

    print("Sorting Options:")
    print("1. Sort by id")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        process_table.sorter(lambda process: process.id)
        process_table.display_table()
    elif choice == 2:
        process_table.sorter(lambda process: process.time)
        process_table.display_table()
    elif choice == 3:
        process_table.sorter(lambda process: process.priority)
        process_table.display_table()
    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
