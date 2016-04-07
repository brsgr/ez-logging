## Synopsis

This wrapper is meant to streamline basic logging in python to 1-2 line commands and avoid direct use of the logging
library

## Example

This primarily revolves around the ezlogging.Log class. log_format is the same as the format attribute for the standard
logging library. Level is the same as the attribute for the logging class. It accepts one of six inputs. The default
values are shown below

```
class Log(object):
    # Base wrapper class for generating log messages
    def __init__(self, msg, log_format='%(asctime)s - %(levelname)s - %(message)s', level='INFO'):
        self.msg = msg
        self.level = level
        self.log_format = log_format
        self.level_dict = {'CRITICAL': 50, 'ERROR': 40, 'WARNING': 30, 'INFO': 20, 'DEBUG': 10, 'NOTSET': 0}
```
***
***
There are 3 primary methods for this class
***

```
import ezlogging as ez

a = ez.Log('hello world')
a.console_logging()

>>2016-04-07 13:24:17,244 - INFO - hello world
```

outputs the log message to console

---


```
import ezlogging as ez

a = ez.Log('hello world')
a.to_file_logging('log_directory', 'logfilename.log', partition='DAY')
```
saves the logs to directory specificed in the first argument with the file name in the second argument. The optional
'partition' argument specifies if the method should automatically create subdirectories for 'YEAR', 'MONTH', 'DAY' or
'HOUR'. If left blank, it will simply save the file to the log_directory argument

---

```
import ezlogging as ez

a = ez.Log('hello world')
a.console_to_file_logging('log_directory', 'logfilename.log', partition='DAY')
```
 outputs to both console and file
