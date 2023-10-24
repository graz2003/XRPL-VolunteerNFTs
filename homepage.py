
import streamlit as st
from PIL import Image


#nav-bar
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ("Home", "Mint NFTs", "About Us"))

#hero
st.image(Image.open('xrpl-twitter-card.png'))
st.markdown("<h1 style='text-align: center; color: black;'>XRPL NFT Volunteer Tokens</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: black;'>Take your volunteer hours with you wherever you go. 🙋🥇 </p>", unsafe_allow_html=True )

st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

st.markdown("<h2 style='text-align: center; color: purple;'> Blockchain Built for Business </h2>", unsafe_allow_html=True)
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.markdown("<p style='text-align: center;'> The XRP Ledger (XRPL) is a decentralized, public blockchain led by a global community of businesses and developers looking to solve problems and create value. </p>", unsafe_allow_html=True)

with col3:
    st.write(' ')

st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

#features
st.title("What are NFTs?")
st.write("NFTs (Non-Fungible Tokens) represent a revolutionary form of digital ownership on the blockchain. Each NFT is a unique, indivisible digital asset, making them ideal for verifying authenticity and ownership of digital or physical items, from digital art to collectibles. Our NFT Volunteer Token Minting project is more than just a platform; it's a celebration of the invaluable work done by volunteers. By minting NFTs, we aim to recognize and reward these unsung heroes, while also fostering a sense of community and collaboration. Join us in this innovative venture, where NFTs not only hold monetary value but also symbolize gratitude, social impact, and the power of giving back. Your involvement in this project helps turn volunteer efforts into lasting digital legacies.")

st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

st.markdown("<h2 style='text-align: center; color: purple;'>Tokenize Gratitude: Celebrating Volunteers with NFTs</h1>", unsafe_allow_html=True)



#minting

st.write("Welcome to our NFT Volunteer Token Minting platform.")
st.write("Mint NFTs to recognize the efforts of our volunteers! Your volutneer tokens will be issued and the records will be stored on the XRPL blockchain so your volutneers can access their records anytime, anywhere.")

firstName = st.text_input('Volunteer First Name', 'John')
lastName = st.text_input('Volunteer Last Name', 'Doe')
wallet = st.text_input('Wallet Address', '1A1zP1eP5QGefi2DMPTfTL5SLmv7DivfNa')
org = st.text_input('Organization', 'YMCA Canada')
hourNum = st.text_input('Number of Hours', '50 hours')
description = st.text_input('Short Description', '')
st.button("Submit")

st.write(' ')
st.write(' ')
st.write(' ')
st.write(' ')

#about

st.markdown("<h2 style='text-align: center; color: black;'>About Us</h1>", unsafe_allow_html=True)
st.write("Transparency within the charity space is important to us.")
st.write("Reach out to volutneerNFTs@gmail.com for more information.")




