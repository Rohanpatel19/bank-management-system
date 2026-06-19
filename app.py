import streamlit as st
from bank import Bank

st.set_page_config(
    page_title="Bank Management System",
    page_icon="🏦",
    layout="wide"
)

st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Choose Option",
    [
        "Create Account",
        "Deposit",
        "Withdraw",
        "View Account"
    ]
)

# CREATE ACCOUNT

if menu == "Create Account":

    st.subheader("Create New Account")

    name = st.text_input("Name")
    age = st.number_input("Age", 18, 100)
    email = st.text_input("Email")
    pin = st.text_input(
        "4 Digit PIN",
        type="password"
    )

    if st.button("Create"):

        if len(pin) != 4:
            st.error("PIN must be 4 digits")

        else:

            acc = Bank.create_account(
                name,
                age,
                email,
                pin
            )

            st.success(
                f"Account Created Successfully!"
            )

            st.info(
                f"Account Number: {acc}"
            )

# DEPOSIT

elif menu == "Deposit":

    st.subheader("Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input(
        "PIN",
        type="password"
    )

    amount = st.number_input(
        "Amount",
        min_value=1
    )

    if st.button("Deposit"):

        user = Bank.authenticate(
            acc,
            pin
        )

        if user:

            Bank.deposit(
                acc,
                amount
            )

            st.success(
                f"₹{amount} Deposited Successfully"
            )

        else:
            st.error("Invalid Credentials")

# WITHDRAW

elif menu == "Withdraw":

    st.subheader("Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input(
        "PIN",
        type="password"
    )

    amount = st.number_input(
        "Amount",
        min_value=1
    )

    if st.button("Withdraw"):

        user = Bank.authenticate(
            acc,
            pin
        )

        if user:

            success = Bank.withdraw(
                acc,
                amount
            )

            if success:
                st.success(
                    f"₹{amount} Withdrawn Successfully"
                )

            else:
                st.error(
                    "Insufficient Balance"
                )

        else:
            st.error(
                "Invalid Credentials"
            )

# VIEW ACCOUNT

elif menu == "View Account":

    st.subheader("Account Details")

    acc = st.text_input(
        "Account Number"
    )

    pin = st.text_input(
        "PIN",
        type="password"
    )

    if st.button("Show Details"):

        user = Bank.authenticate(
            acc,
            pin
        )

        if user:

            st.json(
                {
                    "Name": user["name"],
                    "Email": user["email"],
                    "Balance": user["balance"]
                }
            )

        else:
            st.error(
                "Invalid Credentials"
            )