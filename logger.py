from rich.console import Console

console = Console()


def get_console() -> Console:
    return console


def log(msg: str, *args, **kwargs):
    console.print(msg, *args, **kwargs)


def warn(msg: str, *args, **kwargs):
    console.print(msg, style="#24273a on #eed49f", *args, **kwargs)


def error(msg: str, *args, **kwargs):
    console.print(msg, style="#24273a on #ed8796", *args, **kwargs)


def info(msg: str, *args, **kwargs):
    console.print(msg, style="#7dc4e4", *args, **kwargs)
