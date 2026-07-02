# J&L Operations Discord Inventory Uploader
This is a small project I've made which utilises the [J&L Operations Prep Center API](http://jandloperations.com/) to import stock directly from a Discord bot. 

### How To Setup:
- Download the main.py file into a code editor (Visual Studio)
- Replace the values of `jlKey` and the `bot token`
- Push this to a server/discord bot hosting service (Pebblehost, Repl.it, VPS etc.)

### Discord Usage:
- Type in `/add_prep_stock` and click the pop-up
- Complete *at least* the required parameters for a valid response
- CLick enter and let the code do the rest

### Improvements/Upgrades:
- Move the data from harcoded to a .env file for added security
- Add a function/feature for multiple items at the same time
- Add a feature to remove items (in cases such as cancelled orders etc.)

### Notes:
- This code is extremely basic and acts as a substitute for their web panel (ideally meant for mobile/on-the-go uploads)
- If you have any suggestions/requests etc. please contact me via `contact@humza.vip`
