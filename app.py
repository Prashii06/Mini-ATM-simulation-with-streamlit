import streamlit as st

# Initialize session state for pin and balance
if 'pin' not in st.session_state:
    st.session_state.pin = ''
if 'balance' not in st.session_state:
    st.session_state.balance = 0

# Define functions for ATM operations
def create_pin():
    user_pin = st.text_input("Enter your new PIN:", type="password")
    user_balance = st.number_input("Enter your initial balance:", min_value=0, step=1)
    if st.button("Create PIN"):
        st.session_state.pin = user_pin
        st.session_state.balance = user_balance
        st.success("PIN created successfully!")

def check_balance():
    user_pin = st.text_input("Enter your PIN to check balance:", type="password")
    if st.button("Check Balance"):
        if user_pin == st.session_state.pin:
            st.success(f"Your balance is: ₹{st.session_state.balance}")
        else:
            st.error("Incorrect PIN!")

def change_pin():
    old_pin = st.text_input("Enter your old PIN:", type="password")
    new_pin = st.text_input("Enter your new PIN:", type="password")
    if st.button("Change PIN"):
        if old_pin == st.session_state.pin:
            st.session_state.pin = new_pin
            st.success("PIN changed successfully!")
        else:
            st.error("Incorrect old PIN!")

def withdraw():
    user_pin = st.text_input("Enter your PIN to withdraw money:", type="password")
    amount = st.number_input("Enter amount to withdraw:", min_value=0, step=1)
    if st.button("Withdraw"):
        if user_pin == st.session_state.pin:
            if amount <= st.session_state.balance:
                st.session_state.balance -= amount
                st.success(f"₹{amount} withdrawn successfully! Remaining balance: ₹{st.session_state.balance}")
            else:
                st.error("Insufficient balance!")
        else:
            st.error("Incorrect PIN!")
def main_menu():
    op=st.selectbox("Choose an option:",["create PIN","Check balance","Change pin","Withdraw money","Exit"])
    if op == "create PIN":
        create_pin()
    elif op == "Check balance":
        check_balance()
    elif op == "Change pin":
        change_pin()
    elif op == "Withdraw money":
        withdraw()
    elif op == "Exit":
        st.write("Thank u for using the ATM!")
        return

st.title("ATM system")
main_menu()
