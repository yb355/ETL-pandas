import time
import os
from shutil import move


def notifier(message):
    def wraps(function):
        def inner(*args):
            result = function(*args)
            print(message)
            return result
        return inner
    return wraps

class ComandLineProcessor_Excel:
    def __init__(self, input_f, history_f) -> None:
        self.input = input_f
        self.history = history_f

    def create_file(self, pd):
        print("Starting the application....")
        try:
           self.filename = [f for f in os.listdir(self.input) if not f.startswith(".")][0]
        except IndexError:
            print("Error: No files found in the directory")
            exit()
        print(f"File {self.filename} is found")
        answ = input("Default sheet?: [Yy/Nn] ")
        header = int(input("Index of the column row?: "))
        full_file_name = os.path.join(self.input, self.filename)
        while True:
            if answ.lower() == "n":
                sheet_name = input("What is the sheet name?: ")
                try:
                    raw_df = pd.read_excel(full_file_name, sheet_name=sheet_name, header=header-1)
                    return raw_df
                except:
                    print("Error: sheet name is wrong, try again")
            else:
                try: 
                    raw_df = pd.read_excel(full_file_name, header=header-1)
                    return raw_df
                except:
                    raise

    @staticmethod 
    def column_to_letter_mapper():
        letters = range(65, 91)
        indexes = range(0, 26)
        storage = tuple(chr(i) for i in letters) 
        store_two = tuple(("{}{}".format(chr(i), chr(j)) for i in range(65,79) for j in letters))
        storage = storage + store_two
        indexes = range(0, len(storage))
        return dict(zip(storage, indexes))

    def parse_required_columns(self, df):
        all_excel = type(self).column_to_letter_mapper()
        while True:
            sku = input("Letter for the Excel sku column: ")
            buffer = input("Letter for the Excel buffer column: ")
            try:
                df["SKU"] = df.iloc[:, all_excel[sku]]
                df["Buffer"] = df.iloc[:, all_excel[buffer]]
                return df
            except:
                answ = input("Error: Unable to process: invalid index, exit or try again [t/e]:  ")
                if answ.lower() =="e":
                    exit()

    @notifier("The program is completed.")
    def move_files(self):
        destination = os.path.join(self.history, self.filename)
        origin = os.path.join(self.input, self.filename) 
        print("Please, close Excel if open.")
        time.sleep(3)
        while True:
            try:
                move(origin, destination)
                return
            except PermissionError:
                input("Close Excel before proceeding further. Press Enter to retry.")

               
