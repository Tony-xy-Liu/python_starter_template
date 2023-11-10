import os, sys
import argparse

from .utils import NAME, VERSION, ENTRY_POINTS
from .implementation import some_fn

CLI_ENTRY = ENTRY_POINTS[0]

def _line():
    try:
        width = os.get_terminal_size().columns
    except:
        width = 32
    return "="*width
    
class ArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        self.print_help(sys.stderr)
        self.exit(2, '\n%s: error: %s\n' % (self.prog, message))

class CommandLineInterface:
    @classmethod
    def run(cls, args):
        parser = ArgumentParser(
            prog = f'{CLI_ENTRY} outpost',
        )
        parser.add_argument('-a', '--param_a', metavar='PATH', help="describe the command", required=True)
        parser.add_argument('-b', '--param_b', action='store_true', default=False, help="am optional boolean flag", required=False)
        parsed_args = parser.parse_args(args)

        some_fn(parsed_args.param_a, parsed_args.param_b)

    @classmethod
    def another_function(cls, args):
        some_fn()

    @classmethod
    def help(cls, args=None):
        help = [
            f"{NAME} v{VERSION}",
            f"https://github.com/USER/{NAME}",
            f"",
            f"Syntax: {CLI_ENTRY} COMMAND [OPTIONS]",
            f"",
            f"Where COMMAND is one of:",
        ]+[f"- {k}" for k in COMMANDS]+[
            f"",
            f"for additional help, use:",
            f"{CLI_ENTRY} COMMAND -h/--help",
        ]
        help = "\n".join(help)
        print(help)
COMMANDS = {k:v for k, v in CommandLineInterface.__dict__.items() if k[0]!="_"}

def main():
    if len(sys.argv) <= 1:
        CommandLineInterface.help()
        return

    COMMANDS.get(# calls command function with args
        sys.argv[1], 
        CommandLineInterface.help # default
    )(sys.argv[2:])

if __name__ == "__main__":
    main()
