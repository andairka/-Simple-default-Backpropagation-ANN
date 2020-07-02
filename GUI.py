# This program uses a GUI to get three test
# scores and display their average.

import tkinter


class GUI:
    def __init__(self):
        # Create the main window.
        self.main_window = tkinter.Tk()

        # Create the five frames.
        self.propagation_frame = tkinter.Frame(self.main_window)
        self.accuracy_frame = tkinter.Frame(self.main_window)
        self.button_frame = tkinter.Frame(self.main_window)

        # Create and pack the widgets for test 1.
        self.propagation_label = tkinter.Label(self.propagation_frame,
                                               text='Enter number of iterations')
        self.propagation_entry = tkinter.Entry(self.propagation_frame,
                                               width=10)
        self.propagation_label.pack(side='left')
        self.propagation_entry.pack(side='left')

        # Create and pack the widgets for the average.
        self.result_label = tkinter.Label(self.accuracy_frame,
                                          text='Accuracy:')
        self.accuracy = tkinter.StringVar()  # To update avg_label
        self.accuracy_label = tkinter.Label(self.accuracy_frame,
                                            textvariable=self.accuracy)
        self.result_label.pack(side='left')
        self.accuracy_label.pack(side='left')

        # Create and pack the button widgets.
        self.calc_button = tkinter.Button(self.button_frame,
                                          text='Accuracy',
                                          command=self.calc_accuracy())
        self.quit_button = tkinter.Button(self.button_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.calc_button.pack(side='left')
        self.quit_button.pack(side='left')

        # Pack the frames.
        self.propagation_frame.pack()
        self.accuracy_frame.pack()
        self.button_frame.pack()

        # Start the main loop.
        tkinter.mainloop()

    # The calc_avg method is the callback function for
    # the calc_button widget.

    def calc_accuracy(self):
        # Get the three test scores and store them
        # in variables.
        self.propagation = self.propagation_entry.get()

        #
        # # Calculate the average.
        # self.average = (self.test1 + self.test2 +
        #                 self.test3) / 3.0
        #
        # # Update the avg_label widget by storing
        # # the value of self.average in the StringVar
        # # object referenced by avg.
        # self.avg.set(self.average)
        self.accuracy.set('100%')


# Create an instance of the TestAvg class.
gui = GUI()




