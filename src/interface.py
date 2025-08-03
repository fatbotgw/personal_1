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
        # Get values from inputs and update output
        # You'll implement your puzzle logic here
        output_widget = self.query_one("#output", Static)
        output_widget.update("Current: [yellow]CHECKING...[/]")