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
