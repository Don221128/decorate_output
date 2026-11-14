# easy_decorate_output(edo)
python 3.15+

This version add `keyboard_input` and class `es`.

eg:

```python
from edo import edo,es
edo=edo()
es=es()
edo.set_theme(decorate="*",only_decorate="start",color="green")
edo.decorate_print("Hello!Edo.")
user_name=edo.decorate_input("Enter your name:",decorate="|")
edo.decorate_box(f"Welcome{user_name}.",title="Welcome")
edo.keyboard_input("Pass N",key="N")
es.setting(
    setting="""
    title="Hi!"
    text="This is text."
    """
)
```