import random
from textual.app import App, ComposeResult
from textual.widgets import Static, Input, Button, Header, Footer
from textual.containers import Horizontal, Vertical


class SettingsPuzzle(App):
    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]
    target_value = random.randint(1, 101)

    def compose(self) -> ComposeResult:
        yield Header()
        yield Footer()
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
        
        self.box = Static("INCORRECT VALUE!")
        self.box.styles.background = "red"
        self.box.styles.color = "black"
        self.box.styles.padding = (1, 2)
        self.box.styles.opacity = 0.0
        yield self.box
    
    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.theme = (
            "textual-dark" if self.theme == "textual-light" else "textual-light"
        )

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Event handler called when a button is pressed."""
        if event.button.id == "update_btn":
            self.update_output()
    
    # def on_input_changed(self, event):
    #     # Real-time updates as user types
    #     self.update_output()
    
    def update_output(self):
        try:
            # Get values from the three inputs
            val1 = int(self.query_one("#setting1", Input).value or 0)
            val2 = int(self.query_one("#setting2", Input).value or 0) 
            val3 = int(self.query_one("#setting3", Input).value or 0)
            
            # Your puzzle logic here - example:
            target_sum = self.target_value  # or whatever your target is
            current_sum = val1 + val2 + val3
            
            output_widget = self.query_one("#output", Static)
            if current_sum == target_sum:
                output_widget.update("Current: [green]SUCCESS![/]")
                self.box.update("CORRECT VALUE")
                self.box.styles.background = "green"
                self.box.styles.color = "white"
                self.box.styles.opacity = 1.0
                self.box.styles.animate("opacity", value=0.0, duration=3.0)
            else:
                output_widget.update(f"Current: [red]Sum is {current_sum}, need {target_sum}[/]")
                self.box.update("INCORRECT VALUE!")
                self.box.styles.background = "red"
                self.box.styles.color = "black"
                self.box.styles.opacity = 1.0
                self.box.styles.animate("opacity", value=0.0, duration=3.0)
                
        except ValueError:
            # Handle non-numeric input
            output_widget = self.query_one("#output", Static)
            output_widget.update("Current: [red]Please enter numbers[/]")

    # def on_mount(self):
    #     self.box.styles.animate("opacity", value=0.0, duration=3.0)