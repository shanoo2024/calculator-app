from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivymd.app import MDApp

Window.size = (420, 780)


class CalcRoot(BoxLayout):
    pass


class CalculatorApp(MDApp):
    display_text = StringProperty("0")

    def build(self):
        self.title = "Calculator"
        self.theme_cls.theme_style = "Dark"
        return Builder.load_file("ui.kv")

    def press(self, key):
     if key == "AC":
        self.clear()
        return

    # جلوی اضافه شدن '=' به نمایشگر را بگیر
     if key == "=":
        self.equals()
        return

     if self.display_text == "0" and key not in [".", ")", "%"]:
        self.display_text = ""

     key = {
        "÷": "/",
        "×": "*",
        "−": "-"
    }.get(key, key)

     if key == "%":
        self.display_text += "/100"
     else:
        self.display_text += str(key)

    def clear(self):
        self.display_text = "0"

    def equals(self):
        try:
            expr = self.display_text.strip()
            allowed = set("0123456789+-*/(). ")
            if any(ch not in allowed for ch in expr):
                raise ValueError("Invalid characters")
            result = eval(expr, {"__builtins__": None}, {})
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            self.display_text = str(result)
        except Exception:
            self.display_text = "Error"


if __name__ == "__main__":
    CalculatorApp().run()
