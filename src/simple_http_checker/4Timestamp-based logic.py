# Loops through the log entries, find file error files.
# Writes only the error entries to a file called errors.log.
# Print "Recent error found" then Print "Finished processing logs" when complete.

logs = [
    "2026-08-01 09:15:00 INFO Service started",
    "2026-08-01 09:20:00 ERROR Database connection failed",
    "2026-08-01 09:25:00 INFO Health check passed",
    "2026-08-01 09:30:00 ERROR API timeout"
]
with open("errors.log", "w") as file:
    for log in logs:
        if "ERROR" in log:
            file.write(log)

print("Finished processing logs")
