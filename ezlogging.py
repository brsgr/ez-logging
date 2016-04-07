import logging
import os
import datetime


def directory_dater(log_root, date, partition=''):
    # This function is used to create directories within some root log directory. It will create directories according
    # To YEAR, MONTH, Day, or hour. The default 'time_parition' is day

    partition = partition.upper()
    if partition not in ('DAY', 'YEAR', 'MONTH', 'HOUR', ''):  # Raise value error if kwarg is not valud
        raise ValueError('time_parition must be one of YEAR, MONTH, DAY, or HOUR')
    
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
    def __init__(self, msg, log_format='%(asctime)s - %(levelname)s - %(message)s', level='INFO'):
        self.msg = msg
        self.level = level
        self.log_format = log_format
        self.level_dict = {'CRITICAL': 50, 'ERROR': 40, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10, 'NOTSET': 0}

    def console_logging(self):  # For printing to the console
        logging.basicConfig(level=self.level_dict[self.level], format=self.log_format)
        getattr(logging, self.level.lower())(self.msg)

    def to_file_logging(self, log_root, name, partition=''):  # For printing to file
        # Log root is the root of the log directory, which further breaks down by year, month, day, and hour
        # Depending on how partition is set

        direct = directory_dater(log_root, datetime.datetime.now(), partition=partition)
        logging.basicConfig(filename=direct+'\\'+name, level=self.level_dict[self.level], format=self.log_format)
        getattr(logging, self.level.lower())(self.msg)

    def console_to_file_logging(self, log_root, name, partition=''): # calls both console and to file logging
        self.console_logging()
        self.to_file_logging(log_root, name, partition=partition)


if __name__ == '__main__':
    a = Log('hello world')
    a.to_file_logging('C:\\TEMP\\logroot', 'mylogfile.log', partition='DAY')