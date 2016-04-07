import ezlogging as ez

a = ez.Log('hello world')
a.console_logging()

b = ez.Log('This is an important message', log_format='(asctime)s - (message)s', level='DEBUG')
a.to_file_logging('C:\\TEMP\\samplelogging', 'samplelog', partition='DAY')

c = ez.Log('Combo Message', log_format='(asctime)s - (message)s')
c.console_to_file_logging('C:\\TEMP\\samplelogging', 'combolog')