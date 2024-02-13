import reflex as rx
from link_bio.styles.styles import Size as Size

def navbar() -> rx.Component:
    return rx.hstack(
        rx.text(
            "roswel47",
            height="40px",
            color="white"
        ),
        position="sticky",
        top="0",
        bg="MidnightBlue",
        padding_x=Size.DEFAULT.value,
        padding_y=Size.SMALL.value,
        z_index="999"
    )