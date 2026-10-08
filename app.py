import easy_decorate_output
import edo
edo.set_theme_color("green")
easy_decorate_output.decorate_input("testing.testing","*")
easy_decorate_output.decorate_input("testing.testing","*",only_decorate="start",color="red")
easy_decorate_output.decorate_input("texting.testing","*",only_decorate="end",color="green")
edo.decorate_box("line 1","*",title="test")
edo.test