from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.core.window import Window

Window.clearcolor = (1, 1, 1, 1)

class HourSplitApp(App):
    def build(self):
        self.title = 'Arcon Hour Split'
        
        # Main layout
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Input grid
        input_grid = GridLayout(cols=2, spacing=10, size_hint_y=None, height=200)
        
        # Total Hours
        input_grid.add_widget(Label(text='Total Hours:', color=(0, 0, 0, 1), size_hint_x=0.4))
        self.entry_hours = TextInput(multiline=False, input_filter='int', size_hint_x=0.6)
        input_grid.add_widget(self.entry_hours)
        
        # Total Days
        input_grid.add_widget(Label(text='Total Days:', color=(0, 0, 0, 1), size_hint_x=0.4))
        self.entry_days = TextInput(multiline=False, input_filter='int', size_hint_x=0.6)
        input_grid.add_widget(self.entry_days)
        
        # Hour Option 1
        input_grid.add_widget(Label(text='Hour Option 1:', color=(0, 0, 0, 1), size_hint_x=0.4))
        self.entry_option1 = TextInput(multiline=False, input_filter='int', size_hint_x=0.6)
        input_grid.add_widget(self.entry_option1)
        
        # Hour Option 2
        input_grid.add_widget(Label(text='Hour Option 2\n(optional):', color=(0, 0, 0, 1), size_hint_x=0.4))
        self.entry_option2 = TextInput(multiline=False, size_hint_x=0.6)
        input_grid.add_widget(self.entry_option2)
        
        main_layout.add_widget(input_grid)
        
        # Buttons
        button_layout = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        calc_btn = Button(text='Calculate', background_color=(0.2, 0.6, 1, 1))
        calc_btn.bind(on_press=self.calculate)
        button_layout.add_widget(calc_btn)
        
        clear_btn = Button(text='Clear', background_color=(1, 0.4, 0.4, 1))
        clear_btn.bind(on_press=self.clear_all)
        button_layout.add_widget(clear_btn)
        
        main_layout.add_widget(button_layout)
        
        # Output display with ScrollView
        scroll = ScrollView(size_hint=(1, 1))
        self.output = Label(text='', color=(0, 0, 0, 1), markup=True, 
                           size_hint_y=None, halign='left', valign='top',
                           padding=(10, 10))
        self.output.bind(texture_size=self.output.setter('size'))
        scroll.add_widget(self.output)
        
        main_layout.add_widget(scroll)
        
        return main_layout
    
    def show_error(self, message):
        popup = Popup(title='Error',
                     content=Label(text=message),
                     size_hint=(0.8, 0.3))
        popup.open()
    
    def calculate(self, instance):
        try:
            hours = int(self.entry_hours.text)
            days = int(self.entry_days.text)
            h1 = int(self.entry_option1.text)
            h2_input = self.entry_option2.text
        except:
            self.show_error("Please enter valid numbers.")
            return
        
        result_text = ""
        
        if h2_input.strip() == "":
            found = False
            for h2 in range(2, 9):  # Try for 2 to 8 hours
                for x in range(days + 1):
                    y = days - x
                    total = x * h1 + y * h2
                    if total == hours:
                        found = True
                        result_text += f"[b]• {x} days of {h1} hours[/b]\n"
                        result_text += f"[b]• {y} days of {h2} hours[/b]\n\n"
                        result_text += "Breakdown:\n"
                        result_text += f"• {x} × {h1} = {x*h1} hours\n"
                        result_text += f"• {y} × {h2} = {y*h2} hours\n"
                        result_text += f"\n[color=00ff00]• Total = {x*h1} + {y*h2} = {total} hours ✅[/color]\n"
                        result_text += "-" * 35 + "\n\n"
            if not found:
                result_text = "[color=ff0000]❌ No valid combinations found (2-8 hours tried for Option 2).[/color]\n"
        else:
            try:
                h2 = int(h2_input)
            except:
                self.show_error("Hour Option 2 must be a number or left blank.")
                return
            
            results_found = False
            for x in range(days + 1):
                y = days - x
                total = x * h1 + y * h2
                if total == hours:
                    results_found = True
                    result_text += f"[b]• {x} days of {h1} hours[/b]\n"
                    result_text += f"[b]• {y} days of {h2} hours[/b]\n\n"
                    result_text += "Breakdown:\n"
                    result_text += f"• {x} × {h1} = {x*h1} hours\n"
                    result_text += f"• {y} × {h2} = {y*h2} hours\n"
                    result_text += f"\n[color=00ff00]• Total = {x*h1} + {y*h2} = {total} hours ✅[/color]\n"
                    result_text += "-" * 35 + "\n\n"
            if not results_found:
                result_text = "[color=ff0000]❌ No valid combinations found.[/color]\n"
        
        self.output.text = result_text
    
    def clear_all(self, instance):
        self.entry_hours.text = ''
        self.entry_days.text = ''
        self.entry_option1.text = ''
        self.entry_option2.text = ''
        self.output.text = ''

if __name__ == '__main__':
    HourSplitApp().run()
