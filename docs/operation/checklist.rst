Standard Operation Checklist
****************************

☐ Check the Roomba for physical defects: check the +14-18vDC battery for signs of wear or swelling. Do not proceed if the battery is in a compromised state.

☐ Check the Roomba for electrical issues: check the +14-18vDC battery voltage. It should read less than 18.2v. Do not proceed if the battery is excessively drained or overcharged.

☐ Check the Roomba for physical defects: ensure both wheels spin freely (or as freely as possible with the gear ratio) and that they move up and down sufficiently easily. Hall effect sensors are not configured to provide feedback (physical or logical). Do not proceed if the wheels do not spring freely.

☐ Check the Roomba for physical defects: ensure the bumper at the front moves freely. It should not bind when pressed and should spring back freely after being pressed from any angle. Do not proceed if the bumper and casing is not in good physical shape.

☐ Power on your wireless router and wait for it to fully boot.

☐ Connect the computer to wireless router (either over WiFi or over Ethernet using built-in switch).

☐ Power the motor driver by connecting the +14-18vDC XT90 male connector to the battery's XT90 female connector.

☐ Boot up Raspberry Pi by connecting to +5vDC over USB Type-A. Wait up to 60 seconds for full boot.

☐ Power up the speaker off of its internal battery.

☐ Connect the Raspberry Pi to the wireless network from the wireless router. If this was previously set to automatically connect, you should just wait for it to connect and be assigned a DHCP address.

☐ SSH into the Raspberry Pi via the IP address provided to it by the router.

☐ Check the Roomba for logical defects: run the preliminary motor testing script. The left motor should move forwards for 3 seconds, then backwards for 3 seconds. Then, the right motor should move forwards for 3 seconds, then backwards for 3 seconds. Do not proceed if the test fails.

☐ Check the Roomba for logical defects: run the secondary motor testing script. The left and right motors should counter-rotate relative to each other for 3 seconds in one direction, then 3 direction in the opposite direction. Do not proceed if the test fails to run both motors concurrently.

☐ If all pre-run tests have passed, run the main `roomba.py` script.

During execution, Ctrl+C immediately breaks the program. The momentary pushbutton on the robot itself breaks the program at the next available opportunity.
