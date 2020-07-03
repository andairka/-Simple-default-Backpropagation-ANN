import tkinter
import tkinter.messagebox
from ANN import ANN


class GUI:
    def __init__(self):
        self.main_window = tkinter.Tk()
        self.main_window.title("TITANIC")

        self.propagation_frame = tkinter.Frame(self.main_window)
        self.accuracy_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        self.propagation_label = tkinter.Label(self.propagation_frame,
                                               text='Enter number of iterations')
        self.propagation_entry = tkinter.Entry(self.propagation_frame,
                                               width=10)
        self.propagation_label.pack(side='left')
        self.propagation_entry.pack(side='left')

        self.result_label = tkinter.Label(self.accuracy_frame,
                                          text='Accuracy:')
        self.accuracy = tkinter.StringVar()  # To update avg_label
        self.accuracy_label = tkinter.Label(self.accuracy_frame,
                                            textvariable=self.accuracy)
        self.result_label.pack(side='left')
        self.accuracy_label.pack(side='left')

        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Accuracy',
                                          command=self.calc_accuracy)
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        self.propagation_frame.pack()
        self.accuracy_frame.pack()
        self.button_frame.pack()

        tkinter.mainloop()

    def calc_accuracy(self):
        self.propagation = self.propagation_entry.get()
        if self.propagation == '':
            tkinter.messagebox.showinfo(
                'Attenzione',
                'No value for number of iteration was found. Used default 1000 iteration.'
            )
            self.propagation = '1000'
        ann = ANN()
        ann.trainNetwork(int(self.propagation))
        result = str(ann.accuracy()) + '%'
        self.accuracy = self.accuracy.set(result)


# Create an instance of the GUI
gui = GUI()
