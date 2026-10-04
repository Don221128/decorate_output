from rich.console import Console
from rich.text import Text
from rich.panel import Panel
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
                string=f"{decorate}{lines[-1]}"
            elif only_decorate=="end":
                string=f"{lines[-1]}{decorate}"
            else:
                string=f"{decorate}{lines[-1]}{decorate}"
            console.print(Text(string,style=color))
        late_line=lines[-1]
        if only_decorate=="start":
            result=f"{decorate}{late_line}"
        elif only_decorate=="end":
            result=f"{late_line}{decorate}"
        else:
            result=f"{decorate}{late_line}{decorate}"
        variable=console.input(Text(result,style=color))
        return variable
    except Exception:
        print("Error!")
def decorate_box(text,decorate,title,only_decorate=None,color=None):
    try:
        text=str(text)
        title=str(title)
        lines=text.split('\n')
        result=[]
        for line in lines:
            if only_decorate=="start":
                string=f"{decorate}{line}"
            elif only_decorate=="end":
                string=f"{line}{decorate}"
            else:
                string=f"{decorate}{line}{decorate}"
            result.append(string)
        final_text="\n".join(result)
        box=Panel(final_text,title=title,border_style=color)
        console.print(box)
    except Exception:
        print("Error!")