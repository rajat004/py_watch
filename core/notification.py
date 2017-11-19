from tkinter import Tk, Label, Button

class Notification:
    def __init__(self):
        pass

    @classmethod
    def send_notifications(cls, activities: list):
        print('_____Triggering event for sending notification. !')
        for act in activities:
            print(act.name, act.utilization)
        root = Tk()
        my_gui = Utilization(root, activities)
        root.mainloop()
        return



class Utilization:
    
    def __init__(self, master: Tk, activities: list):
        self.master = master
        self.activity= activities
        self.activities_labels = list()
        self.process_lables = list()
        self.buttons = list()

        master.title("System Utilizations !")
        for act in activities:
            process = act.CulpritProcess
            self.activities_labels.append(Label(master, text="Alert {0} % {1} utilization !".format(act.utilization, act.name)))
            self.process_lables.append(Label(master, text="Highest {0} consumed by {1} process ({2}%) !".format(act.name , process.name, process.utilization)))
            #self.buttons.append(Button(master, text="kill me", command=lambda :self.kill_process(process.id)))
            self.button = Button(master, text="Quit", command=lambda :self.master.quit())

        # LAYOUT
        row = 0
        column = 0
        for i in range(len(self.activities_labels)):
            self.activities_labels[i].grid(row= row, column= column)
            row += 1
            self.process_lables[i].grid(row= row, column= column)
            #self.buttons[i].grid(row=row, column= column +1)
            row += 1



