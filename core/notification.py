from tkinter import Tk, Label, Button

class Notification:
    def __init__(self):
        pass

    # method for sending notification currently
    # enabled for desktop
    # can be implemented for email also.
    @classmethod
    def send_notifications(cls, activities: list):
        print('_____Triggering event for sending notification. !')
        filter_activities = [act for act in activities if act is not None]
        if  len(filter_activities):
            root = Tk()
            root.geometry('%dx%d+%d+%d' % (300, 100, 500, 350))
            Utilization(root, filter_activities)
            root.mainloop()
        return

class Utilization:
    '''
        class for implementing pop-up/alerts
        when utilization goes beyond threshold
    '''
    
    def __init__(self, master: Tk, activities: list):
        self.master = master
        self.activity= activities
        self.activities_labels = list()
        self.process_lables = list()
        self.buttons = list()

        self.master.title("System Utilizations !")
        for act in activities:
            #process = act.CulpritProcess
            self.activities_labels.append(Label(self.master, text="Alert {0} % {1} utilization !".format(act.utilization, act.name)))
            #self.process_lables.append(Label(master, text="Highest {0} consumed by {1} process ({2}%) !".format(act.name , process.name, process.utilization)))
            #self.buttons.append(Button(master, text="kill me", command=lambda :self.kill_process(process.id)))
            self.button = Button(self.master, text="Close", command=lambda :self.master.destroy())
            self.quit_button = Button(self.master, text="Quit", command=lambda :quit())

        # below method is for setting up layout
        row = 0
        column = 0
        for i in range(len(self.activities_labels)):
            self.activities_labels[i].grid(row= row, column= column)
            #self.process_lables[i].grid(row= row, column= column)
            #self.buttons[i].grid(row=row, column= column +1)
            row += 1
        self.button.grid(row= row+1, column= column)
        self.quit_button.grid(row =row+1 , column = column +1)




