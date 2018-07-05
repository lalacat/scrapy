import optparse
from scrapy.commands import ScrapyCommand
from scrapy.commands.check import Command
from scrapy.settings import BaseSettings
parser = optparse.OptionParser(prog="Command", formatter=optparse.TitledHelpFormatter(), \
                               conflict_handler='resolve')
parser.add_option("--logfile", metavar="FILE",
                  help="log file. if omitted stderr will be used")
parser.add_option("--nolog", action="store_true",
                  help="disable logging completely")

parser.add_option("--profile", metavar="FILE", default=None,
                  help="write python cProfile stats to FILE")
parser.add_option("--pidfile", metavar="FILE",
                  help="write process ID to FILE")
parser.add_option("-s", "--set", action="append", default=[], metavar="NAME=VALUE",
                 help="set/override setting (may be repeated)")

arg = ['--logfile=test.txt', '--profile=test2.txt','-sa=b']
opts, args = parser.parse_args(arg)

print(args)
print(opts)
com = Command()
com.settings = BaseSettings()
sc= ScrapyCommand()
com.process_options(args,opts)
p1 = com.settings.attributes
p2 = com.settings.get("LOG_FILE")
cs = com.settings
print(type(cs.attributes["LOG_FILE"]))
