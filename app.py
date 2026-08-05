import streamlit as st

# 1. Database of bakery recipes (Add your 25 recipes here)
recipes = {
    "Chocolate Cake": {
        "unit": "kg",
        "ingredients": {"Flour": (250, "g"), "Sugar": (200, "g"), "Cocoa Powder": (50, "g"), "Eggs": (4, "pcs")}
    },
    "Puff Pastry": {
        "unit": "pieces",
        "ingredients": {"Flour": (40, "g"), "Master Puff": (782/30, "g"), "Astra": (4, "g"), "Sugar": (0.6, "g"), "Salt": (0.4, "g"), "Water": (20, "g")}
    },
    "White Bread": {
        "unit": "kg",
        "ingredients": {"Bread Flour": (600, "g"), "Water": (380, "ml"), "Yeast": (10, "g")}
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
