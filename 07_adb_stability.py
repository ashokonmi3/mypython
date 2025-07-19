# Approch
# “My approach to detect Android device stability would be structured in three steps:”

# 1️⃣ Check if the device is connected
# “First, I will run adb get-state to check
#  if the device is connected and recognized by ADB. 
# If the device is not connected, I stop and report that no device is available.”

# 2️⃣ Check if the device has completed booting
# “If the device is connected, I will run adb shell 
#  sys.boot_completed. This will tell me if the device has finished booting.
#  A value of 1 means boot is complete, and 0 means it is still booting or stuck.”

# 3️⃣ Check if the device is responsive
# “Finally, I will run a simple command like adb shell 
# uptime to confirm that the device responds to shell commands. 
# If I get valid output, the device looks stable. 
# If not, I report that the device might be unresponsive or unstable.”

# 4️⃣ Summarize the result
# “At each step, I print clear messages about the device’s state — whether it’s connected, booted, and responsive.”



# We import subprocess so we can run ADB commands from Python
import subprocess

# We import time in case we want to add delays (not used in this basic version but good to have)
import time

# We define a function that will check if the device is stable
def check_android_stability():
    """
    This function:
    - Checks if a device is connected to ADB
    - Checks if the device has finished booting
    - Checks if the device responds to a simple shell command
    """

    # Step 1: Check if the device is connected to ADB
    # We use 'adb get-state' which tells us if the device is connected 
    # (should return 'device')
    result = subprocess.run(
        ["adb", "get-state"],       # The command we want to run
        capture_output=True,        # This means we want to capture its output so we can read it
        text=True                   # This means the output will be a string, not bytes
    ) comment likho

    # We get the output of the command and remove extra spaces or newlines
    state = result.stdout.strip()

    # We check if the output was "device" (this means the device is connected)
    if state != "device":
        print("❌ Device is not connected or not detected by ADB.")
        return  # Stop the function here — no point in continuing

    # If we are here, device is connected
    print("✅ Device is connected to ADB.")

    # Step 2: Check if the device has finished booting
    # We run: adb shell getprop sys.boot_completed
    # This will return "1" if booting is finished
    result = subprocess.run(
        ["adb", "shell", "getprop", "sys.boot_completed"],
        capture_output=True,
        text=True
    )

    # Get and clean the output
    boot_status = result.stdout.strip()

    # Check the value
    if boot_status != "1":
        print("⚠️ Device boot not completed — it may still be booting or unstable.")
        return  # Stop the function because boot is not done

    print("✅ Device boot completed successfully.")

    # Step 3: Check if the device responds to a basic shell command
    # We'll run 'adb shell uptime' — it prints system uptime 
    # (how long the device has been running)
    result = subprocess.run(
        ["adb", "shell", "uptime"],
        capture_output=True,
        text=True
    )

    # If the command ran successfully (return code 0 means success)
    if result.returncode == 0:
        print("✅ Device is responding to shell commands — looks stable.")
        print(f"ℹ️ Uptime info: {result.stdout.strip()}")  # Print the uptime info
    else:
        print("❌ Device is not responding to shell commands — may be unstable or stuck.")

# Call (run) the function to perform the checks
check_android_stability()
