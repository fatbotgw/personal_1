from textual.app import App
from textual.widgets import Static, Input, Button
from textual.containers import Horizontal, Vertical

class SettingsPuzzle(App):
    def compose(self):
        with Horizontal():
            with Vertical():
                yield Static("Settings:")
                yield Input(placeholder="Setting 1 (0-100)", id="setting1")
                yield Input(placeholder="Setting 2 (0-100)", id="setting2") 
                yield Input(placeholder="Setting 3 (0-100)", id="setting3")
                yield Button("Update", id="update_btn")
            with Vertical():
                yield Static("Target: [green]SUCCESS[/]")
                yield Static("Current: [red]FAIL[/]", id="output")
    
    def on_button_pressed(self, event):
        if event.button.id == "update_btn":
            self.update_output()
    
    def on_input_changed(self, event):
        # Real-time updates as user types
        self.update_output()
    
    def update_output(self):
        try:
            # Get values from the three inputs
            val1 = int(self.query_one("#setting1", Input).value or 0)
            val2 = int(self.query_one("#setting2", Input).value or 0) 
            val3 = int(self.query_one("#setting3", Input).value or 0)
            
            # Your puzzle logic here - example:
            target_sum = 150  # or whatever your target is
            current_sum = val1 + val2 + val3
            
            output_widget = self.query_one("#output", Static)
            if current_sum == target_sum:
                output_widget.update("Current: [green]SUCCESS![/]")
            else:
                output_widget.update(f"Current: [red]Sum is {current_sum}, need {target_sum}[/]")
                
        except ValueError:
            # Handle non-numeric input
            output_widget = self.query_one("#output", Static)
            output_widget.update("Current: [red]Please enter numbers[/]")