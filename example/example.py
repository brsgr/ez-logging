import ezlogging as ez

a = ez.Log('hello world')

a.console_logging()
a.to_file_logging('C:\\TEMP', 'samplelog')