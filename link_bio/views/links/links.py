import reflex as rx
from link_bio.components.link_button import link_button
from link_bio.components.title import title
from link_bio.styles.styles import Size as Size

def links() -> rx.Component:
    return rx.vstack(
        title("Canales de Información"),
        link_button(
            "Twitch",
            "Canal de infromacion en general",
            "https://www.twitch.tv/roswel47"
        ),
        link_button(
            "Youtube",
            "Cursos y Tutoriales",
            "https://www.youtube.com/@roswel47"
        ),
        link_button(
            "Github",
            "Repositorios de codigos",
            "https://github.com/gregoriocarrillo"
        ),
        title("Canales de Información"),
        link_button(
            "Twitch",
            "Canal de infromacion en general",
            "https://www.twitch.tv/roswel47"
        ),
        link_button(
            "Youtube",
            "Cursos y Tutoriales",
            "https://www.youtube.com/@roswel47"
        ),
        link_button(
            "Github",
            "Repositorios de codigos",
            "https://github.com/gregoriocarrillo"
        ),
        width="100%",
        spacing=Size.DEFAULT.value
    )