import RPi.GPIO as GPIO
import keyboard

# GPIO setup
LED_PIN = 22
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

try:
    print("Press and hold the spacebar to turn on the LED, release to turn it off.")
    print("Press Escape to exit.")
    while True:
        if keyboard.is_pressed('space'):
            GPIO.output(LED_PIN, GPIO.HIGH)  # Turn on LED
        else:
            GPIO.output(LED_PIN, GPIO.LOW)   # Turn off LED

        if keyboard.is_pressed('esc'):
            print("\nEscape key pressed. Exiting program.")
            break

except KeyboardInterrupt:
    print("\nExiting program")

finally:
    GPIO.cleanup()  # Clean up GPIO
