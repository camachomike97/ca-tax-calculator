from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.utils import platform

class TaxCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 30
        self.spacing = 20

        self.add_widget(Label(text='California Sales Tax Calculator',
                              font_size=26,
                              bold=True,
                              size_hint_y=None,
                              height=70))

        self.add_widget(Label(text='7.25% California Sales Tax',
                              font_size=18,
                              color=(0.95, 0.6, 0.1, 1)))

        self.add_widget(Label(text='Enter pre-tax amount ($):', font_size=20))

        self.amount_input = TextInput(multiline=False,
                                      font_size=22,
                                      input_filter='float',
                                      hint_text='100.00')
        self.add_widget(self.amount_input)

        calc_btn = Button(text='Calculate Tax',
                          font_size=22,
                          size_hint_y=None,
                          height=70,
                          background_color=(0.12, 0.45, 0.85, 1))
        calc_btn.bind(on_press=self.calculate)
        self.add_widget(calc_btn)

        self.result_label = Label(text='Your total will appear here',
                                  font_size=24,
                                  bold=True,
                                  color=(0, 0.65, 0.2, 1))
        self.add_widget(self.result_label)

    def calculate(self, instance):
        try:
            amount = float(self.amount_input.text or 0)
            if amount < 0:
                self.result_label.text = "Please enter a positive number"
                return
            TAX_RATE = 0.0725
            total = amount * (1 + TAX_RATE)
            self.result_label.text = f'Total with tax:\n${total:,.2f}'
        except:
            self.result_label.text = "Invalid number. Try again."

class TaxApp(App):
    def build(self):
        if platform == 'android':
            Window.size = (400, 700)
        else:
            Window.size = (420, 650)
        return TaxCalculator()

if __name__ == '__main__':
    TaxApp().run()
    