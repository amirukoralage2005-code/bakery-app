import streamlit as st

# 1. Database of bakery recipes (Add your 25 recipes here)
recipes = {
    "Puff Pastry": {
        "unit": "pieces",
        "ingredients": {"Flour": (40, "g"), "Master Puff": (782/30, "g"), "Astra": (4, "g"), "Sugar": (0.6, "g"), "Salt": (0.4, "g"), "Water": (20, "g")}
    },
    "Date Cake": {
        "unit": "kg",
        "ingredients": {"Dates": (400, "g"), "Baking Soda": (0.66, "tsp"), "Water": (0.66, "tsp"),"Flour": (166, "g"),"Astra": (166, "g"),"Sugar": (166, "g"),"Egg": (166, "g"),"Milk Powder": (50, "g"),"Baking Powder": (1.25, "tsp")}
    },
    "Chicken Pie": {
        "unit": "pieces",
        "ingredients": {"Flour": (1100/30, "g"), "Astra": (550/30, "g"), "Sugar": (4.416/30, "tsp"),"Salt": (4.416/30, "tsp"),"Egg": (2.64/30, "eggs"),"Water": (0, "as needed")}
    },
    "Mini Pizza": {
        "unit": "pieces",
        "ingredients": {"Flour": (300/10, "g"), "Yeast": (0.66/10, "tsp"), "Water": (0.66/10, "tsp"),"Salt": (0.66/10, "tsp"),"Sugar": (0.6/10, "tsp"),"Olive Oil": (1.5/10, "tbsp")}
    },
    "Eclair": {
        "unit": "pieces",
        "ingredients": {"Flour": (500/50, "g"), "Astra": (500/50, "g"), "Sugar": (6.6/50, "tsp"),"Salt": (2/50, "tsp"),"Water": (1000/50, "g"),"Egg": (13/50, "eggs")}
    },
    "Danish Pastry": {
        "unit": "pieces",
        "ingredients": {"Flour": (500/10, "g"), "Astra": (50/10, "g"), "Yeast": (7.5/10, "g"),"Sugar": (50/10, "g"),"Milk Powder": (20/10, "g"),"Egg": (1/10, "eggs"),"Master Puff": (250/10, "g"),"Salt": (4.5/10, "g"),"Water": (225/10, "g")}
    }

}

# 2. Application UI
st.title("Bakery Recipe Calculator")

selected_item = st.selectbox("Select Recipe", list(recipes.keys()))
item_data = recipes[selected_item]

quantity = st.number_input(f"Enter quantity ({item_data['unit']})", min_value=0.1, value=1.0, step=0.5)

st.divider()
st.subheader(f"Ingredients for {quantity} {item_data['unit']} of {selected_item}:")

for name, (amount, unit) in item_data["ingredients"].items():
    total = amount * quantity
    st.write(f"- **{name}**: {total:.2f} {unit}")
