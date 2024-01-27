import reflex as rx
import datetime

def footer() -> rx.Component:
    return rx.vstack(
        rx.image(src="favicon.ico"),
        rx.link(
            f"© {datetime.date.today().year} GREGORIO CARRILLO",
            href="https://github.com/gregoriocarrillo"
        ),
        rx.text(" - TODOS LOS DERECHOS RESERVADOS")
    )