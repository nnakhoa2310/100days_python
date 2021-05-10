# import tkinter as tk
#
# window = tk.Tk()
# window.title("GUI Python")
# window.minsize(width=500, height=300)
#
# my_label = tk.Label(text="Im a label", font=("Arial", 24, "bold"))
# my_label.pack()
#
# window.mainloop()

# method unlimited agruments
#
# def add(*args):
#     sum = 0
#     for n in args:
#         sum += n
#     print(sum)
# add(2,4,3,2,5)

# method keyword unlimited agruments

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
my_car = Car(make = "Nissan",model = "FDS9")
print(my_car.make)