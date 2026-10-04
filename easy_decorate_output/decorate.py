from rich.console import Console
from rich.text import Text
console=Console()
def decorate_print(text,decorate,only_decorate=None,color=None):
    try:
        text=str(text)
        lines=text.split('\n')
        for line in lines:
            if only_decorate=="start":
                string=f"{decorate}{line}"
            elif only_decorate=="end":
                string=f"{line}{decorate}"
            else:
                string=f"{decorate}{line}{decorate}"
            if color!=None:
                string=f"[{color}]{string}[/]"
            console.print(string)
    except Exception:
        print("Error!")
def decorate_input(text,decorate,only_decorate=None,color=None):
    try:
        text=str(text)
        lines=text.split('\n')
        for line in lines[:-1]:
            if only_decorate=="start":
                print(f"{decorate}{line}")
            elif only_decorate=="end":
                print(f"{line}{decorate}")
            else:
                print(f"{decorate}{line}{decorate}")
            if color!=None:
                variable=f"[{color}]{line}[/]"
        if only_decorate=="start":
            print(f"{decorate}{lines[-1]}")
        elif only_decorate=="end":
            print(f"{lines[-1]}{decorate}")
        else:
            print(f"{decorate}{lines[-1]}{decorate}")
        variable=console.input(Text(lines[-1],style=color))
        return variable
    except Exception:
        print("Error!")