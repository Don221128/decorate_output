lazy from rich.console import Console
lazy from rich.text import Text
lazy from rich.panel import Panel
lazy from rich.style import Style
lazy import keyboard
console=Console()
theme_color="white"
theme_only_decorate=None
theme_decorate=None
theme_box_size=None
def decorate_print(text=None,decorate=None,only_decorate=None,color=None,end="/n"):
    try:
        global theme_color
        global theme_only_decorate
        global theme_decorate
        if decorate==None:
            decorate=theme_decorate
        if only_decorate==None:
            only_decorate=theme_only_decorate
        if color is None:
            color=theme_color
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
            console.print(string,end=end)
    except Exception:
        print("Error!")
def decorate_input(text=None,decorate=None,only_decorate=None,color=None,end="/n"):
    try:
        global theme_color
        global theme_only_decorate
        global theme_decorate
        if decorate==None:
            decorate=theme_decorate
        if only_decorate==None:
            only_decorate=theme_only_decorate
        if color is None:
            color=theme_color
        lines=text.split("\n")
        for _ in lines[:-1]:
            if only_decorate=="start":
                string=f"{decorate}{lines[-1]}"
            elif only_decorate=="end":
                string=f"{lines[-1]}{decorate}"
            else:
                string=f"{decorate}{lines[-1]}{decorate}"
            console.print(Text(string,style=color,end=end))
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
def decorate_box(title=None,text=None,decorate=None,only_decorate=None,size=None,color=None):
    try:
        global theme_color
        global theme_only_decorate
        global theme_decorate
        global theme_box_size
        if decorate==None:
            decorate=theme_decorate
        if only_decorate==None:
            only_decorate=theme_only_decorate
        if size==None:
            size=theme_box_size
        if color is None:
            color=theme_color
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
        if size is not None:
            width=max(3,size[0])
            height=max(3,size[1])
        else:
            width,height=150,5
        box=Panel(final_text,title=title,width=width,height=height,border_style=color)
        console.print(box)
    except Exception as e:
        print(f"Error!{e}")
def set_theme(decorate=None,only_decorate=None,box_size=None,color=None):
    global theme_color
    global theme_only_decorate
    global theme_decorate
    global theme_box_size
    if decorate==None:
        theme_decorate=None
    else:
        theme_decorate=decorate
    if only_decorate==None:
        theme_only_decorate=None
    else:
        theme_only_decorate=only_decorate
    if box_size==None:
        theme_box_size=None
    else:
        theme_box_size+box_size
    if color==None:
        theme_color="white"
    else:
        Style.parse(color)
        theme_color=color
def keyboard_input(text=None,decorate=None,only_decorate=None,key=None,color=None,end="\n"):
    global theme_color
    global theme_only_decorate
    global theme_decorate
    if decorate==None:
        decorate=theme_decorate
    if only_decorate==None:
        only_decorate=theme_only_decorate
    if color==None:
        color=theme_color
    lines=text.split("\n")
    for _ in lines[:-1]:
        if only_decorate=="start":
            string=f"{decorate}{lines[-1]}"
        elif only_decorate=="end":
            string=f"{lines[-1]}{decorate}"
        else:
            string=f"{decorate}{lines[-1]}{decorate}"
        console.print(Text(string,style=color,end=end))
    while keyboard.is_pressed(key):
        event=keyboard.read_event()
        if event.event_type==keyboard.KEY_DOWN():
            if key is not None:
                if event.name in key:
                    passed_key=event.name
                    break
            else:
                passed_key=event.name
    return passed_key