from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class ProfitCalculator(BoxLayout):
    def __init__(self, **kwargs):
        super(ProfitCalculator, self).__init__(**kwargs)
        self.orientation = 'vertical'

        # Header row
        header = GridLayout(rows=1, cols=4, size_hint_y=None, height=30)
        header.add_widget(Label(text="Продукты"))
        header.add_widget(Label(text="Цена"))
        header.add_widget(Label(text="%"))
        header.add_widget(Label(text="Расчет"))
        self.add_widget(header)

        # Input rows
        self.product_entries = []
        self.price_entries = []
        self.margin_entries = []
        self.final_price_entries = []

        for i in range(30):
            row = GridLayout(rows=1, cols=4, size_hint_y=None, height=65)

            product_entry = TextInput(multiline=False)
            self.product_entries.append(product_entry)
            row.add_widget(product_entry)

            price_entry = TextInput(multiline=False)
            self.price_entries.append(price_entry)
            row.add_widget(price_entry)

            margin_entry = TextInput(multiline=False)
            self.margin_entries.append(margin_entry)
            row.add_widget(margin_entry)

            final_price_entry = TextInput(text='', multiline=False)
            self.final_price_entries.append(final_price_entry)
            row.add_widget(final_price_entry)

            self.add_widget(row)

        # Calculate button
        calculate_button = Button(text="Рассчитать все")
        calculate_button.bind(on_press=self.calculate_all)
        self.add_widget(calculate_button)

    def calculate_all(self, instance):
        for i in range(30):
            try:
                price = float(self.price_entries[i].text)
                margin = float(self.margin_entries[i].text)
                final_price = price + (price * margin / 100)
                self.final_price_entries[i].text = f"{final_price:.2f}"
            except ValueError:
                continue

class ProfitApp(App):
    def build(self):
        return ProfitCalculator()

if __name__ == "__main__":
    ProfitApp().run()