# initialize infinite keywords
def __init__(self, **kwargs):
    # call grid layout constructor
    super(TheGridLayout, self).__init__(**kwargs)

    # set columns
    self.cols = 1

    # set an embedded grid within the "main grid"
    self.top_grid = GridLayout()
    self.top_grid.cols = 2

    # add input text
    self.top_grid.add_widget(Label(text="Name: ",
                                   size_hint_y=None,
                                   height=50,
                                   size_hint_x=None,
                                   width=700
                                   ))

    self.name = TextInput(multiline=False,
                          size_hint_y=None,
                          height=50,
                          size_hint_x=None,
                          width=500
                          )

    self.top_grid.add_widget(self.name)

    # add top widget to the App
    self.add_widget(self.top_grid)

    # add button
    self.submit = Button(text="Submit",
                         size_hint_y=None,
                         height=50,
                         size_hint_x=None,
                         width=100
                         )
    self.submit.bind(on_press=self.press)  # bind the button to the function self.press()
    self.add_widget(self.submit)
