import os
from lib.AbstractDataSource import AbastractDataSource

class FilesSources(AbastractDataSource):

    def __init__(self):
        self.previous_files = []
        self.start()


    def create_path(self):
        current_directory = os.getcwd()
        self.folder_path = os.path.join(current_directory, 'data')
        if not os.path.exists(self.folder_path):
            os.makedirs(self.folder_path)


    def check_for_new_files(self):
        current_files = os.listdir(self.folder_path)
        new_files = [file for file in current_files if file not in self.previous_files]
        
        if new_files:
            print(f"New files found: {new_files}")

            self.previous_files = current_files

        else:
            print("No new files found")

    def get_data(self):
        pass

    def transform_data_to_df(self):
        pass

    def save_data(self):
        pass

    def show_files(self):
        print(self.previous_files)


    def start(self):
        self.create_path()
    
    
