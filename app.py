import easy_decorate_output
import edo
edo.set_theme(color="green")
easy_decorate_output.decorate_input("testing.testing","*")
easy_decorate_output.decorate_input("testing.testing","*",only_decorate="start",color="red")
easy_decorate_output.decorate_input("texting.testing","*",only_decorate="end",color="green")
edo.decorate_box("line 1","*",title="test 1")
edo.decorate_box("line 2","*",title="test 2")
for _ in range(50):
    for _ in range(50):
        edo.fast_print("█",end="")
print()