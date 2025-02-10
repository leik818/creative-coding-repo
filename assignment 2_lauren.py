def setup():
    size(400, 400)
    background ("#00008B")
    
def draw():
    no_stroke()
    fill ("#FFDE21")
    circle(70, 175, 118)    
    circle(198, 175, 118)
    
    rect(270, 120, 40, 118)
    rect(310, 120, 40, 30)
    rect(310, 165, 40, 30)
    
    fill("#00008B")
    circle (70, 175, 50)
    circle(198, 175, 50)
    
def key_pressed (e):
    key_value= e.get_key()
    if key_value == 's' or key_value=='S':
        save('assignment_2.jpg')
    
run_sketch()
    
    
    