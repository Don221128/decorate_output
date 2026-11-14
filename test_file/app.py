import easy_decorate_output
import edo
edo.set_theme(color="green")
easy_decorate_output.decorate_input("testing.testing","*")
easy_decorate_output.decorate_input("testing.testing","*",only_decorate="start",color="red")
easy_decorate_output.decorate_input("texting.testing","*",only_decorate="end",color="green")
edo.keyboard_input("Pass E","",key="e")