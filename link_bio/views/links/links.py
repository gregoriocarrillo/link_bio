import reflex as rx
from link_bio.components.link_button import link_button

def links() -> rx.Component:
    return rx.vstack(
        link_button("Twitter", "https://twitter.com/roswel47"),
        link_button("Youtube", "https://www.youtube.com/@GregCarrillo77"),
        link_button("Instagram", "https://www.instagram.com/gcm_fotografia")
    )