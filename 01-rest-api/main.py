from fastapi import FastAPI
from enum import Enum

app = FastAPI()

@app.get("/hello")
async def hello():
    return "Welcome Python ML FastAPI QuickStart /hello Get All... "

@app.get("/hello/{name}")
async def hello(name):
    return f"Welcome {name}! Python FastAPI QuickStart /hello/{name} Get All... "


food_menu = {
    'american' : ["Burger", "Hot Dog", "Apple Pie"],
    'indian' : ["Samosa", "Paratha Subji", "Roti Subji"],
    'italian' : ["Pizza", "Macroni", "Pasta"]
}

valid_cuisines = food_menu.keys()

@app.get("/food/{cuisine}")
async def get_food(cuisine):
    if(cuisine not in valid_cuisines):
        return f"Supported Cuisines = {valid_cuisines}"
    return food_menu.get(cuisine)

class AvailableCuisines(str, Enum):
    american = 'american'
    indian = 'indian'
    italian = 'italian'

@app.get("/cuisine/{cuisine}")
async def get_cuisine(cuisine: AvailableCuisines):
    return food_menu.get(cuisine)

coupons = {
    1: '10%',
    2: '20%',
    3: '30%'
}

@app.get("/coupon/{code}")
async def get_coupon(code: int):
    return { 'Discount_Coupon': coupons.get(code)}

