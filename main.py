import discord
from discord import app_commands
import requests

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

jlKey = "put your JL API token here"
headers = {
        "x-api-key": jlKey, 
        "Content-Type": "application/json"
    }

@tree.command(name="add_prep_stock", description="Add stock")
@app_commands.describe(
    title="Title",
    sku="SKU",
    qty="Qty",
    order_number="Order Number",
    dangerous_goods="Dangerous Goods",
    meltable="Meltable",
    bubble_wrap="Bubble Wrap",
    label_removal="Remove Labels",
    polybag="Polybag",
    bundle="Bundle Instructions",
    addons="Addons (comma separated)",
    notes="Notes"
)
async def add_stock(
    interaction: discord.Interaction, 
    title: str, 
    sku: str, 
    qty: int, 
    order_number: str = None, 
    dangerous_goods: bool = False,
    meltable: bool = False,
    bubble_wrap: bool = False,
    label_removal: bool = False,
    polybag: bool = False,
    bundle: str = None,
    addons: str = None, 
    notes: str = None
):
    await interaction.response.defer()
        
    data = {
        "title": title,
        "sku": sku,
        "qty": qty,
        "dangerousGoods": dangerous_goods
    }
    
    if meltable:
        data.setdefault("addons", []).append("Meltable")
    if bubble_wrap:
        data.setdefault("addons", []).append("Bubble Wrap")
    if label_removal:
        data.setdefault("addons", []).append("Label Removal")
    if polybag:
        data.setdefault("addons", []).append("Polybag")
    if bundle:
        data.setdefault("addons", []).append(f"Bundle: {bundle}")
    if order_number:
        data["orderNumber"] = order_number
    if notes:
        data["notes"] = notes
    if addons:
        alist = [x.strip() for x in addons.split(",") if x.strip()]
        if alist:
            data["addons"] = alist
    
    try:
        addStockRequest = requests.post(
            "https://dash.jandloperations.com/customer-api/inbound", 
            headers=headers, 
            json=data, 
            timeout=10
        )
        
        if addStockRequest.status_code != 200:
            await interaction.followup.send(
                f"Failed to add inventory. Status: {addStockRequest.status_code}\n{addStockRequest.text}", 
                ephemeral=True
            )
        else:
            await interaction.followup.send(
                f"Successfully added inventory to J&L. Status: {addStockRequest.status_code}", 
                ephemeral=True
            )
    except:
        await interaction.followup.send("Request failed", ephemeral=True)

@client.event
async def on_ready():
    await tree.sync()
    print(f"{client.user.name} is online")

client.run("put your bot token here")
