input.onButtonPressed(Button.A, function () {
    moveDot("A")
})
input.onButtonPressed(Button.B, function () {
    moveDot("B")
})
function moveDot (button: string) {
    led.unplot(x, y)
    if (button == "A") {
        y += 1
        if (y > 4) {
            y = 0
        }
    } else {
        x += 1
        if (x > 4) {
            x = 0
        }
    }
    led.plot(x, y)
}
let y = 0
let x = 0
x = 0
y = 0
led.plot(x, y)
