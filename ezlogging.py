import logging
import os
import datetime


def directory_dater(log_root, date, partition=''):
    # This function is used to create directories within some root log directory. It will create directories according
    # To YEAR, MONTH, Day, or hour. The default 'time_parition' is day

    partition = partition.upper()
    if partition not in ('DAY', 'YEAR', 'MONTH', 'HOUR', ''):  # Raise value error if kwarg is not valid
        raise ValueError('time_partition must be one of YEAR, MONTH, DAY, or HOUR')
    
    if partition == 'YEAR':  # Generate directory string
        direct = log_root + '\\' + str(date.year)
    elif partition == 'MONTH':
        direct = log_root + '\\' + str(date.year) + '\\' + str(date.strftime('%B'))
    elif partition == 'DAY':
        direct = log_root + '\\' + str(date.year) + '\\' + str(date.strftime('%B')) + '\\' + str(date.year) + '_' + \
                 str(date.month) + '_' + str(date.day)
    elif partition == 'HOUR':
        direct = log_root + '\\' + str(date.year) + '\\' + str(date.strftime('%B')) + '\\' + str(date.year) + '_' + \
                 str(date.month) + '_' + str(date.day) + '\\' + str(date.hour)
    else:  # If partition is not specified, just return the log_root
        direct = log_root

    if not os.path.exists(direct):  # create the directory if it does not exist
        os.makedirs(direct)
    return direct  # return directory name as a string


class Log(object):
    # Base wrapper class for generating log messages
    def __init__(self, msg, log_format='%(asctime)s - %(message)s', level='INFO'):
        self.msg = msg
        self.level = level
        self.log_format = log_format
        self.level_dict = {'CRITICAL': 50, 'ERROR': 40, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10, 'NOTSET': 0}

    def console_logging(self):  # For printing to the console
        l = logging.getLogger('mylog')  # create logger (name is arbitrary since handlers are cleared every iteration)
        formatter = logging.Formatter(self.log_format)  # Set formatting from class definition

        streamHandler = logging.StreamHandler()  # Creates streamhandler (console)
        streamHandler.setFormatter(formatter)

        l.setLevel(self.level)  # Add handlers to Logger
        l.addHandler(streamHandler)

        log1 = logging.getLogger('mylog')
        getattr(log1, self.level.lower())(self.msg)  # calls log1.info, log1.debug etc...

        handlers = l.handlers[:]  # Clears handler with every log file write
        for handler in handlers:
            handler.close()
            l.removeHandler(handler)

    def to_file_logging(self, log_root, log_file, partition=''):  # For printing to file
        direct = directory_dater(log_root, datetime.datetime.now(), partition=partition)  # Directory creator

        l = logging.getLogger('mylog')  # create logger (name is arbitrary since handlers are cleared every iteration)
        formatter = logging.Formatter(self.log_format)  # Set formatting from class definition
        fileHandler = logging.FileHandler(direct + '\\' + log_file, mode='a')  # Creates filehandler
        fileHandler.setFormatter(formatter)

        l.setLevel(self.level)  # Add handlers to Logger
        l.addHandler(fileHandler)

        log1 = logging.getLogger('mylog')
        getattr(log1, self.level.lower())(self.msg)  # calls log1.info, log1.debug etc...

        handlers = l.handlers[:]  # Clears handler with every log file write
        for handler in handlers:
            handler.close()
            l.removeHandler(handler)

    def console_to_file_logging(self, log_root, log_file,partition=''):  # both console and file logging
        direct = directory_dater(log_root, datetime.datetime.now(), partition=partition)  # Directory creator

        l = logging.getLogger('mylog')  # create logger (name is arbitrary since handlers are cleared every iteration)
        formatter = logging.Formatter(self.log_format)  # Set formatting from class definition
        fileHandler = logging.FileHandler(direct + '\\' + log_file, mode='a')  # Creates filehandler
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()  # Creates streamhandler (console)
        streamHandler.setFormatter(formatter)

        l.setLevel(self.level)  # Add handlers to Logger
        l.addHandler(fileHandler)
        l.addHandler(streamHandler)

        log1 = logging.getLogger('mylog')

        getattr(log1, self.level.lower())(self.msg)  # calls log1.info, log1.debug etc...

        handlers = l.handlers[:]  # Clears handler with every log file write
        for handler in handlers:
            handler.close()
            l.removeHandler(handler)




if __name__ == '__main__':
    pass