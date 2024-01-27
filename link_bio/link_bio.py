import reflex as rx

class State(rx.State):
    pass 

def index() -> rx.Component:
    return rx.hstack(
        rx.text(
            "roswel47",
            height="40px"
        )
    )

app = rx.App()
app.add_page(index)
