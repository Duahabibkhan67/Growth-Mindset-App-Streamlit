import streamlit as st 

st.set_page_config(page_title="Growth Mindset Project", page_icon="⭐")

st.title("Growth Mindset Challenge: 🌱")

st.header("🚀 Welcome To Your Growth Journey!")
st.write("Embrace the challenges, unlock your potential difference, and start your growth mindset journey today! 🌟")

# Quote section
st.header("💡 Today's Growth Mindset Quote")
st.write("“Success is not the key to happiness. Happiness is the key to success.” -Albert Schweitzer")


if st.button('Inspire Me with Another Quote'):
    st.write("“The only way to do great work is to love what you do.” - Steve Jobs")

# Challenge section
st.header("🔧 What's Your Challenge Today?")
user_input = st.text_input("Describe your challenge you're facing:")


if st.button('Submit Challenge'):
    if user_input:
        st.success(f" You are facing: {user_input}. Keep pushing forward towards your goals! 🚀")
    else:
        st.warning("Please enter your challenge to continue! ⭐")

# Reflection section
st.header("Reflect on Your Challenge")
reflection = st.text_area("Write your reflection here:")


if st.button('Submit Reflection'):
    if reflection:
        st.success(f" ✨Great Insight! Your reflection: {reflection}")
    else:
        st.info("Reflecting on past challenges can help you grow!🌟")

# Achievement section
st.header("🏆 Celebrate Your Wins!")
achievement = st.text_input("Share something you've recently achieved:")


if st.button('Celebrate My Achievement'):
    if achievement:
        st.success(f"🎉 Congratulations! You Achieved: {achievement}")
    else:
        st.info("Big or Small, every achievement counts! 🎊")
        

st.balloons()

# Footer
st.write("- - -")
st.write("🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟")

st.write("** Made by Dua Habib😉**")
st.write("Connect With Me On [LinkedIn](https://www.linkedin.com/in/dua-habib-497557301/?originalSubdomain=pk)")
