import eel

eel.init('web')

@eel.expose
def cuber():
    print("I am in Python cuber!")
    return(27)


eel.start("index.html", size=(600,600))
