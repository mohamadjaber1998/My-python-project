class Filter:
    def __init__(self):
        self.names = []
        self.filter_names()

    def filter_names(self):

        with open('Input/my_names/invited_names.txt', "r") as file:
            names_before_edite = file.readlines()

        for name in names_before_edite:
            final_name = name.strip()
            self.names.append(final_name)
