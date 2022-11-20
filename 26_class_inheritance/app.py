class Device:
    def __init__(self, name, connected_by):
        self.name = name
        self.connected_by = connected_by
        self.connected = True

    def __str__(self):
        return f"Device {self.name!r} ({self.connected_by})"

    def disconnect(self):
        self.connected = False
        print("Disconnected.")


printer = Device("Printer", "USB")
print(printer)
printer.disconnect()


class Printer(Device):
    def __init__(self, name, connected_by, page_capacity):
        super().__init__(name, connected_by)
        self.page_capacity = page_capacity
        self.remaining_capacity = page_capacity

    def __str__(self):
        return f"{super().__str__()} ({self.remaining_capacity} pages remaining)"

    def print(self, pages):
        if not self.connected:
            print("Your printer is not connected!")
            return

        print(f"Printing {pages} pages.")
        self.remaining_capacity -= pages


printer = Printer("Printer", "USB", 500)
printer.print(18)

print(printer)

printer.disconnect()
printer.print(10)