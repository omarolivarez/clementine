import eel

eel.init('web')

@eel.expose
def cuber(number):
    return number**3


eel.start("index.html", size=(600,350))
