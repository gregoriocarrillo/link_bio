import reflex as rx
from link_bio.components.link_icon import link_icon
from link_bio.components.info_text import info_text
from link_bio.styles.styles import Size as Size

def header() -> rx.Component:
    return rx.vstack(
        rx.hstack(
            rx.avatar(name="Gregorio Carrillo", size="xl"),
            rx.vstack(
                rx.heading(
                    "GREGORIO CARRILLO",
                    size="lg"
                ),
                rx.text(
                    "@roswel47",
                    margin_top="0px !important"
                ),
                rx.hstack(
                    link_icon("https://twitter.com/roswel47"),
                    link_icon("https://www.instagram.com/gcm_fotografia"),
                    link_icon("https://github.com/gregoriocarrillo")
                ),
                
                align_items="start"
            ),
            spacing=Size.DEFAULT.value
        ),

        rx.flex(
            info_text("+10", "años de experiencia"),
            rx.spacer(),
            info_text("+10", "años de experiencia"),
            rx.spacer(),
            info_text("+10", "años de experiencia"),
            width="100%"
        ),

        rx.text("Soy un entusiasta desarrollador web y formándome en ciberseguridad. Adicional soy fotógrafo profesional y corredor de seguros, feliz esposo y padre de 2 niñas. Aquí encontrarán enlaces de interés"),
        spacing=Size.BIG.value,
        align_items="start"
    )