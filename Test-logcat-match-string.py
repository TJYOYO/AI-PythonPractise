import subprocess


def monitor_adb_log_for_string(target_string):
    try:
        # Start adb logcat process
        adb_process = subprocess.Popen(
            ["adb", "logcat"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            universal_newlines=True,
            bufsize=1
        )

        print(f"Monitoring ADB log for string: {target_string}")

        # Loop to continuously read the log output
        while True:
            # Read a line from the log
            line = adb_process.stdout.readline()

            if target_string in line:
                print(f"Found: {line.strip()}")

    except FileNotFoundError:
        print("ADB not found. Ensure it is installed and added to the system PATH.")
    except KeyboardInterrupt:
        print("\nScript interrupted by user. Terminating...")
    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Clean up: Terminate the adb process
        adb_process.terminate()


if __name__ == "__main__":
    target_string = "[CarInfoUpdater] update"
    monitor_adb_log_for_string(target_string)
