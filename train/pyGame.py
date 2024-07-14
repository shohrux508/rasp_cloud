import turtle
import keyboard

keyboard.add_hotkey('w', lambda: turtle.forward(10))
keyboard.add_hotkey('s', lambda: turtle.backward(10))
keyboard.add_hotkey('a', lambda: turtle.left(90))
keyboard.add_hotkey('d', lambda: turtle.right(90))
keyboard.add_hotkey('1', lambda: turtle.speed(5))
keyboard.add_hotkey('2', lambda: turtle.speed(10))
keyboard.add_hotkey('3', lambda: turtle.speed(0))

turtle.exitonclick()
