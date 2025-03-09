# app.py
def greet(name):
    return f"Hello, {name}!"

def main():
    # Run the greeting function
    print(greet("World"))
    # Keep the script running
    import time
    while True:
        time.sleep(20)

if __name__ == '__main__':
    main()
