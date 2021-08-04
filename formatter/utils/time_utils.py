import datetime

class CurrentDateTime:

    def __init__(self) -> None:
        self.current_datetime = datetime.datetime.now()        

    def zero_remover(f):
        def inner(*args):
            result = f(*args)
            result = result.lstrip("0")
            return result
        return inner
    
    @property
    def current_datetime(self):
        return self.__current_datetime
    
    @current_datetime.setter
    def current_datetime(self, value):
        self.__current_datetime = value

    def month_name(self):
        return self.current_datetime.strftime("%b")

    def day(self):
        return self.current_datetime.strftime("%d")

    @zero_remover
    def month(self):
        return self.current_datetime.strftime("%m")
    
    def year(self):
        return self.current_datetime.strftime("%Y")

    @zero_remover
    def time(self):
        return self.current_datetime.strftime("%I:%M%p")

    def output_format_dd_tt(self):
        date_format = str(self.current_datetime.strftime("%Y%m%d")).replace("-", "")
        time_format = self.current_datetime.strftime("%H%M%S")
        return date_format, time_format