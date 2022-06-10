def on_button_pressed_a():
    moveDot("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    moveDot("B")
input.on_button_pressed(Button.B, on_button_pressed_b)

def moveDot(button: str):
    global y, x
    led.unplot(x, y)
    if button == "A":
        y += 1
        if y > 4:
            y = 0
    else:
        x += 1
        if x > 4:
            x = 0
    led.plot(x, y)
y = 0
x = 0
x = 0
y = 0
led.plot(x, y)