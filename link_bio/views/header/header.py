import reflex as rx

def header() -> rx.Component:
    return rx.vstack(
        rx.avatar(name="Gregorio Carrillo", size="xl"),
        rx.text("@roswel47"),
        rx.text("GREGORIO CARRILLO"),
        rx.text("Soy entusiasta desarrollador web, programador y formándome en ciberseguridad. Adicional soy fotógrafo profesional y corredor de seguros, feliz esposo y padre de 2 niñas. Aquí encontrarán enlaces de interés")
    )