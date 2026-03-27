📝 Instructions for Customizing Your ESP32 BLE Project (BT_Code2_ControllingHarware.py) 

Change Device Name 

Update the ESP32 name (ESP32-Nayan) to something unique, so multiple devices don’t get mixed up during connection. 

Modify Behavior as per your designed harware 

Currently: 

Writing "1" → runs LED Pattern 1 

Writing "2" → runs LED Pattern 2 

You can customize this logic based on your project idea. 

Add more options using elif (e.g., "3", "4", etc.) 

✅ Best practice: 
Create separate functions for each behavior and call them when a specific value is received. 

 

Run Once vs Continuous Execution 

Right now, each pattern runs only once because of: value = "" 
 

If you remove this line, the pattern will run continuously 
until a new value is received from the app. 

💡 Think of this as designing your own “command system” between the app and ESP32. 

 
