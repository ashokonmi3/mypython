# adb devices
# # ✅ Ensure your device is connected

# adb reboot
# # ✅ This reboots the device

# adb wait-for-device
# # ✅ This waits until the device is fully booted and connected again

# adb shell getprop sys.boot_completed
# 👉 adb shell getprop sys.boot_completed → should return 1 if boot completed successfully.


# ✅ How to find problems in reboot
# 👉 After adb wait-for-device, if your device does not appear in adb devices:

# The device might be stuck in boot loop

# The USB connection might have dropped

# The device might require authorization again (check screen for prompt)

# 👉 Use these commands to debug:
# adb devices
# # ✅ Check if device is listed

# adb shell getprop sys.boot_completed
# # ✅ Should print 1 if boot completed, or nothing / 0 if not booted

# adb logcat
# # ✅ Check logs for boot errors

# adb shell dmesg
# # ✅ Kernel logs, might show boot or hardware issues
# ==========================
# 👉 Do we want to reboot the device just once, or multiple times? Should the number of reboots be configurable?

# 👉 After rebooting, do we only need to check if the device is online, or also confirm that it has finished booting (sys.boot_completed)?

# 👉 Do we need to report success/failure for each reboot attempt, or only at the end?

# 👉 What should the program do if the reboot fails? Should it retry or stop?
# =======================
# Approch
# “My approach would be to reboot the device using adb reboot, wait for it to reconnect using adb wait-for-device, 
# and then confirm that the device has finished booting using adb shell getprop sys.boot_completed. I’d do this in a loop for the number of reboots needed, and include error handling in case the device fails to come back online.”
# ================
import subprocess  # We import subprocess to run ADB commands from Python
import time        # We import time so we can pause between operations

# We define a function that will reboot the device a certain number of times
def adb_reboot_simple(times):
    """
    Reboots the device 'times' number of times and checks if boot is completed.
    """

    # Loop through the number of times we want to reboot
    for i in range(times):
        print(f"\nReboot {i + 1} of {times}")  # Print which reboot attempt we are on

        # Send the ADB reboot command
        # This will restart the connected device
        subprocess.run(["adb", "reboot"])
        print("Device is rebooting...")  # Inform the user

        # Wait 2 seconds before we start checking device status
        # This gives the device time to actually start rebooting
        time.sleep(2)

        # Run adb wait-for-device command
        # This will block (pause) until the device comes back online and ADB can see it
        subprocess.run(["adb", "wait-for-device"])
        print("Device is back online.")  # Inform the user

        # Now check if the device has completed booting
        # We run adb shell getprop sys.boot_completed
        # This returns "1" if boot is done, or "0" (or empty) if still booting
        result = subprocess.run(
            ["adb", "shell", "getprop", "sys.boot_completed"],  # Command we run on the device
            capture_output=True,  # Capture what the command prints so we can check it
            text=True  # Make sure we get the output as a string, not bytes
        )

        # Clean up the output: remove spaces or newlines
        status = result.stdout.strip()

        # Check the status and print the result
        if status == "1":
            print("Reboot successful.")  # Device booted successfully
        else:
            print("Device boot not completed yet.")  # Device still booting or something went wrong

# ✅ Call the function — this will reboot the device 2 times
adb_reboot_simple(2)
# ===============


# ---

# ### ⚡ **Time Complexity**

# 👉 The program runs in a loop:

# ```python
# for i in range(times):
# ```

# Where `times = number of reboots requested`.

# 👉 Inside each reboot:

# * `adb reboot` → takes real-world time (depends on device reboot duration)
# * `adb wait-for-device` → blocks until device reconnects (again, real-world duration)
# * `adb shell getprop sys.boot_completed` → constant-time command

# ✅ Therefore:

# 👉 The *computational* time is O(times) because the loop runs `times` times.
# 👉 The actual **wall clock time** depends heavily on:
# * How long each reboot takes
# * How long device takes to reconnect and report boot completion

# ---

# ### ⚡ **Space Complexity**

# 👉 The program uses:

# * A few variables: counters, result from subprocess
# * No data structures that grow with input

# ✅ Therefore:

# {O(1)}


# 👉 The space used does not depend on the number of reboots — it's constant.

# ---

# ### 💡 **How to say it in interview**

# *“The computational time complexity is O(times), where times is the number of reboots requested, because we loop that many times. 
# The space complexity is O(1) because we use a fixed amount of memory regardless of input size. However, actual runtime depends on the real-world duration of each reboot and device reconnect.”*

# ---



