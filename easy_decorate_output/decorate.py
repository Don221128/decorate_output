def decorate_print(text,decorate,only_decorate=None):
    try:
        text=str(text)
        lines=text.split('\n')
        for line in lines:
            if only_decorate=="start":
                print(f"{decorate}{line}")
            elif only_decorate=="end":
                print(f"{line}{decorate}")
            else:
                print(f"{decorate}{line}{decorate}")
    except Exception:
        print("Error!")
def decorate_input(text,decorate,only_decorate=None):
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
        if only_decorate=="start":
            variable=input(f"{decorate}{line}")
        elif only_decorate=="end":
            variable=input(f"{line}{decorate}")
        else:
            variable=input(f"{decorate}{lines[-1]}{decorate}")
        return variable
    except Exception:
        print("Error!")