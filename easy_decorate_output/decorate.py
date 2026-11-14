lazy from rich.console import Console
lazy from rich.text import Text
lazy from rich.panel import Panel
lazy from rich.style import Style
lazy import keyboard
lazy import json
console=Console()
theme_color="white"
theme_only_decorate=None
theme_decorate=None
theme_box_size=None
theme_end="\n"
class edo:
    def __init__(self):
        global theme_color
        global theme_only_decorate
        global theme_decorate
        global theme_box_size
        global theme_end
        self.theme_color=theme_color
        self.theme_only_decorate=theme_only_decorate
        self.theme_decorate=theme_decorate
        self.theme_box_size
        self.theme_end=theme_end
    def decorate_print(self,text=None,decorate=None,only_decorate=None,color=None,end="\n"):
        try:
            if decorate==None:
                decorate=self.theme_decorate
            if only_decorate==None:
                only_decorate=self.theme_only_decorate
            if color is None:
                color=self.theme_color
            if end==None:
                end==self.theme_end
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
    def decorate_input(self,text=None,decorate=None,only_decorate=None,color=None,end="\n"):
        try:
            if decorate==None:
                decorate=self.theme_decorate
            if only_decorate==None:
                only_decorate=self.theme_only_decorate
            if color is None:
                color=self.theme_color
            if end==None:
                end=self.theme_end
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
    def decorate_box(self,title=None,text=None,decorate=None,only_decorate=None,size=None,color=None):
        try:
            if decorate==None:
                decorate=self.theme_decorate
            if only_decorate==None:
                only_decorate=self.theme_only_decorate
            if size==None:
                size=self.theme_box_size
            if color is None:
                color=self.theme_color
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
    def set_theme(self,decorate=None,only_decorate=None,box_size=None,color=None,end=None):
        try:
            if decorate==None:
                self.theme_decorate=None
            else:
                self.theme_decorate=decorate
            if only_decorate==None:
                self.theme_only_decorate=None
            else:
                self.theme_only_decorate=only_decorate
            if box_size==None:
                self.theme_box_size=None
            else:
                self.theme_box_size=box_size
            if end==None:
                self.theme_end="\n"
            else:
                self.theme_end=end
            if color==None:
                self.theme_color="white"
            else:
                Style.parse(color)
                self.theme_color=color
        except Exception as e:
            print(f"Error!{e}")
    def keyboard_input(self,text,decorate,only_decorate,key,color,end="\n"):
        try:
            if decorate==None:
                decorate=self.theme_decorate
            if only_decorate==None:
                only_decorate=self.theme_only_decorate
            if color==None:
                color=self.theme_color
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
        except KeyError as e:
            print(f"Error!{e}")
        except Exception as e:
            print(f"Error!{e}")
class es:
    def __init__(self):
        self.setting_json={}
    def parse_val(self,raw_val):
        val=raw_val.strip()
        if val.lower()=="true":
            return True
        if val.lower()=="false":
            return False
        try:
            return int(val)
        except ValueError:
            pass
        try:
            return float(val)
        except ValueError:
            pass
        return val
    def setting(self,setting):
        try:
            lines=setting.split("\n")
            for line in lines:
                line=line.strip()
                if not line or line.startswith("#") or "=" not in line:
                    continue
                key,val=line.split("=",1)
                self.setting_json[key.strip()]=self.parse_val(val.strip('"/"'))
        except Exception as e:
            print(f"Error!{e}")
    def get_json(self):
        try:    
            return json.dumps(self.setting_json,indent=4,ensure_ascii=False)
        except Exception as e:
            print(f"Error!{e}")