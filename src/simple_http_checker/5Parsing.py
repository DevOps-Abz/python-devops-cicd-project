# Take log lines, split it into pieces. Print only the log level (INFO, WARNING, ERROR).

logs = [
    "2026-08-01 09:15:00 INFO Server started",
    "2026-08-01 09:20:00 ERROR Database connection failed",
    "2026-08-01 09:25:00 WARNING Disk space low",
    "2026-08-01 09:30:00 ERROR API timeout"
]

for log in logs:                                    # <--- Print the time and log level
    parts = log.split()
    print(parts[1], parts[2])


# if parts[2] == "ERROR":                             <--- Print only the ERROR logs
    # print(parts[1], parts[2])