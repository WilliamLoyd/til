with  open("server.log", "r") as source, open("errors.txt", "w") as destination :
    for line in source:
        if "[ERROR]"in line or "[WARN]"in line:
            destination.write(line)
            print(f"Archived: {line.strip()}")
