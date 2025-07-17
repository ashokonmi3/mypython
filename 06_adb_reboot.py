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
# Question  to be asked

# 👉 for this program we may need to run the multiple adb commands
#  Do we need to handle success/failure for each adb command or only reboot attempt or i can write 
# simple code to check reboot?

# =======================
# Approch
# “My approach would be to reboot the device using adb reboot,
#  wait for it to reconnect using adb wait-for-device, 
# and then confirm that the device has finished booting using adb shell
#  getprop sys.boot_completed. I’d do this in a loop for the number of reboots needed, 
# and include error handling in case the device fails to come back online.”
# ================
import subprocess  # We import subprocess to run ADB commands from Python
import time        # We import time so we can pause between operations

# We define a function that will reboot the device a certain number of times
def adb_reboot_simple(times):
    """
    Reboots the device 'times' number of times and checks if boot is completed.
    Also calculates the percentage of successful reboots.
    """
    successful_reboots = 0  # Track the number of successful reboots

    # Loop through the number of times we want to reboot
    for i in range(times):
        print(f"\nReboot {i + 1} of {times}")  # Print which reboot attempt we are on

        # Step 1: Send the ADB reboot command
        # This will restart the connected device
        subprocess.run(["adb", "reboot"])
        print("Device is rebooting...")  # Inform the user

        # Step 2: Wait for the device to come back online after rebooting
        # We wait for 2 seconds before checking device status to allow time for reboot
        time.sleep(2)
# By adding a short delay (sleep(2)), you:

# Give the device some time to properly shut down and start its reboot sequence.

# Help adb wait-for-device sync properly when the device begins to reconnect.
        # Step 3: Run adb wait-for-device command to ensure the device is back online
        subprocess.run(["adb", "wait-for-device"])
        print("Device is back online.")  # Inform the user

        # Step 4: Check if the device has completed booting
        # Run adb shell getprop sys.boot_completed command
        # This returns "1" if boot is done, or "0" (or empty) if still booting
        result = subprocess.run(
            ["adb", "shell", "getprop", "sys.boot_completed"],  # Command to check boot status
            capture_output=True,  # Capture output of the command
            text=True  # Get output as a string (instead of bytes)
        )
# 👉 subprocess.run([...])
# This is a Python function that runs the command provided as a list of strings. It executes the command like it would in the terminal.
# 👉 ["adb", "shell", "getprop", "sys.boot_completed"]
# This is the command you are running:
# adb: The Android Debug Bridge tool used to communicate with the Android device.
# shell: Tells ADB to run the following command inside the device’s shell (as if you are using a terminal on the Android device).
# getprop: A shell command on Android devices that retrieves system properties.
# sys.boot_completed: A specific Android system property that indicates if the device has finished booting.
# It returns "1" if boot is completed.
# Returns nothing or "0" if still booting.

        # Step 5: Check if the output contains '1' (indicating boot is complete)
        if "1" in result.stdout:  # If '1' is found anywhere in the output
            print("Reboot successful.")  # Device booted successfully
            successful_reboots += 1  # Increment successful reboot count
        else:
            print("Device boot not completed yet.")  # Device still booting or something went wrong

    # Step 6: Calculate the success percentage after all reboots
    success_percentage = (successful_reboots / times) * 100

    # Step 7: Output the success rate as a percentage
    print(f"\nSuccess Rate: {success_percentage:.2f}%")  # Print the success rate

# ✅ Call the function — this will reboot the device 2 times
adb_reboot_simple(10)

# ===============
# Approach:
# 1. **Initialization**:
#    - We initialize a counter called `successful_reboots` to 0. This will track the number of reboots that are successful (i.e., when the device finishes booting).

# 2. **Reboot Process**:
#    - **Step 1: Reboot Command**: 
#        - For each reboot attempt, we send the ADB reboot command (`adb reboot`) to restart the device.
#        - This step initiates the reboot process on the connected device.
#    - **Step 2: Wait for Device**: 
#        - After sending the reboot command, we wait for 2 seconds to allow the device to begin the reboot process.
#    - **Step 3: Device Online Check**:
#        - We then use `adb wait-for-device` to make sure the device comes back online. This is important to ensure the device is reachable after reboot.
#    - **Step 4: Check Boot Completion**:
#        - We run the command `adb shell getprop sys.boot_completed` to check the device's boot status.
#        - The command returns:
#          - `"1"`: Boot is complete, meaning the device has finished rebooting.
#          - `"0"` or empty: Boot is still in progress, or there was an issue.
#  
# 3. **Tracking Success**:
#    - If the boot status is `"1"`, we increment the `successful_reboots` counter to track a successful reboot.
#    - If the boot status is `"0"` or empty, the reboot was not successful, and no increment happens.

# 4. **Success Rate Calculation**:
#    - After completing all the reboot attempts, we calculate the success rate:
#        - Formula: `Success Rate = (successful_reboots / total_reboots) * 100`
#        - This gives the percentage of successful reboots out of the total number of attempts.

# 5. **Output**:
#    - Finally, we print the success rate as a percentage to the user, showing how many times the reboot process was completed successfully.


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



