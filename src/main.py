from app import App
from console_io import IO

def main():
    io = IO()
    app = App(io)
    app.run()

if __name__ == "__main__":
    main()