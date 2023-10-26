import panel as pn

stylesheet = """
    #divContainer input[type="file"] {
      border-radius: 4px;
}
"""

def make_layout():
    inp = pn.widgets.FileInput()
    inp.stylesheets=[stylesheet]

    output = pn.widgets.StaticText(value="None")

    def _print_value(e):
        output.value = inp.filename

    btn = pn.widgets.Button(name='Show')
    btn.on_click(_print_value)

    return pn.Column(inp, output, btn)

make_layout().servable(location="test_app")
