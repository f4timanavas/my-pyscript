from pyscript import display, when, document

@when("click", "#show-btn")
def show_name(event):
    name = document.querySelector("#name-input").value
    document.querySelector("#name-display").innerText = f"Greetings {name}!"

