import os
print("Dumblang Interpreter - (c) PartehDev 2023")
settings = {
    "prompt": ">>> ",
    "history_file": "history.txt"
}
if os.path.isfile("settings.txt"):
    with open("settings.txt") as f:
        settings.update(eval(f.read()))
def save_settings():
    with open("settings.txt", "w") as f:
        f.write(repr(settings))
while True:
    try:
        command = input(settings["prompt"])
        if command.startswith("print"):
            text = command[6:].strip()
            if text.startswith("'") and text.endswith("'"):
                print(text[1:-1])
            elif text.startswith('"') and text.endswith('"'):
                print(text[1:-1])
            else:
                try:
                    print(eval(text))
                except:
                    print(f"Error: Invalid expression - {text}")
        elif command.startswith("settings"):
            parts = command.split()[1:]
            if len(parts) == 0:
                print(settings)
            elif len(parts) == 1:
                key = parts[0]
                if key in settings:
                    print(f"{key} = {settings[key]}")
                else:
                    print(f"Error: Unknown setting - {key}")
            elif len(parts) == 2:
                key, value = parts
                try:
                    settings[key] = eval(value)
                    print(f"{key} set to {settings[key]}")
                    save_settings()
                except:
                    print("Error: Invalid value")
            else:
                print("Error: Invalid syntax for 'settings' command")
        elif command.startswith("load"):
            parts = command.split()[1:]
            if len(parts) == 0:
                print("Error: Please specify a filename to load")
            else:
                try:
                    with open(parts[0]) as f:
                        code = f.read()
                        exec(code)
                except Exception as e:
                    print(f"Error: {e}")
        elif command.startswith("quit") or command.startswith("exit"):
            break
        else:
            exec(command)
    except KeyboardInterrupt:
        break
    except Exception as e:
        print(f"Error: {e}")
