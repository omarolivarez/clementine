import pandas

Class Clemen():
    def __init__():
        self.df = 0
        self.cols = []
        self.df_path = ""
        self.history_path = ""
        self.reps_passed = 0
        self.total_reps = 0
        self.stat = ""
        self.selected_column = ""

    def set_df(self, df):
        self.df = df

    def get_df(self):
        return self.df

    def set_columns(self, cols):
        self.columns = cols

    def get_columns(self):
        return self.cols

    def set_df_path(self, path):
        self.df_path = path

    def get_df_path(self):
        return self.df_path

    def set_reps_passed(self, reps_passed):
        self.hreps_passed = reps_passed

    def get_reps_passed(self):
        return self.reps_passed

    def set_total_reps(self, total_reps):
        self.total_reps = total_reps

    def get_total_reps(self):
        return self.total_reps

    def set_history_path(self, path):
        self.history_path = path

    def get_history_path(self):
        return self.history_path

    def set_stat(self, stat):
        self.stat = stat

    def get_stat(self):
        return self.stat

    def set_selected_column(self, selected_column):
        self.selected_column = selected_column

    def get_selected_column(self):
        return self.selected_column
