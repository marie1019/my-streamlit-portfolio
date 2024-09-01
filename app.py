import streamlit as st

st.set_page_config(page_title="Marie's Portfolio", page_icon=":blue_heart:", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("Navigation")
selected_tab = st.sidebar.radio("Go to", ["🏠About Me", "🎨Portfolio 1", "💻Portfolio 2", "📩Contact Me"])
# Footer or additional content
st.sidebar.write("---")
st.sidebar.write("© 2024 by Marie Antoinette B. Paez. All rights reserved.")

# --- MAIN / ABOUT ME ---
if selected_tab == "🏠About Me":
    st.title("About Me")
    
    # Create containers for "About Me" and "My Skills"
    with st.container():
        # "About Me" section
        left_column, right_column = st.columns(2)
        with left_column:
            st.write("""
                    I'm a 4th-year IT student with a focus on full-stack development. My academic work revolves around coding, 
                    but outside of school, I indulge in art as a hobby. My interests span anime and gaming, and while I consider 
                    myself an introvert and shy, I communicate when it's necessary. In both art and coding, I'm still exploring 
                    and developing my style and skills, and hope that it would boost my career either way.
                    """)

            st.write("📄**Name:** Paez, Marie Antoinette B.")
            st.write("💻**Program & Year:** BSIT - 4")
            st.write("🏫**College Attended:** Cebu Institute of Technology - University")
            st.write("📍**Location:** Philippines, Cebu 6000")
            st.write("🎧**Interest:** Anime, Memes, Gaming, Drawing")
          
        with right_column:
          
            st.image("assets//marie.jpg", width=300)
          
    with st.container():
        # "My Skills" section
        st.write("---")
        st.header("My Skills")
        
        left_column, right_column = st.columns(2)
        with left_column:
          st.subheader("💻Technical Skills")
          st.write("""
              - **Frontend Development**: HTML, CSS, JavaScript, React.js, Material UI
              - **Backend Development**: C, C++, Python, Java, Firebase
              - **Fullstack Development**: React.js, Node.js, Python with Django
          """)
        with right_column:
          st.subheader("🎨Design Skills")
          st.write("""
              - **Digital Drawing**: Clip Studio Paint, Paint Tool Sai
              - **Graphic Design**: Adobe Photoshop, Canva
          """)

# --- MY WORK ---
elif selected_tab == "🎨Portfolio 1":
    st.title("🎨Drawing Portfolio")

    selected_tab = st.selectbox("Select a Section", ["Digital Drawings", "Graphic Design", "Tangible Designs", "Downloadables", "Speedpaints"])

    if selected_tab == "Digital Drawings":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("assets//my_work//1.png", use_column_width=True)
            st.image("assets//my_work//2.png", use_column_width=True)
            st.image("assets//my_work//3.1.png", use_column_width=True)
        with col2:
            st.image("assets//my_work//4.png", use_column_width=True)
            st.image("assets//my_work//7.png", use_column_width=True)
            st.image("assets//my_work//3.png", use_column_width=True)
            st.image("assets//my_work//3.2.png", use_column_width=True)
        with col3:
            st.image("assets//my_work//6.png", use_column_width=True)
            st.image("assets//my_work//5.png", use_column_width=True)
            st.image("assets//my_work//3.3.png", use_column_width=True)

    elif selected_tab == "Graphic Design":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("assets//my_work//g3.png", use_column_width=True)
            st.image("assets//my_work//g2.png", use_column_width=True)
            st.image("assets//my_work//g1.png", use_column_width=True)
        with col2:
            st.image("assets//my_work//h3.png", use_column_width=True)
            st.image("assets//my_work//h2.png", use_column_width=True)
            st.image("assets//my_work//h1.png", use_column_width=True)
        with col3:
            st.image("assets//my_work//i2.png", use_column_width=True)
            st.image("assets//my_work//i1.png", use_column_width=True)

    elif selected_tab == "Tangible Designs":
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("assets//my_work//t1.1.png", use_column_width=True)
            st.image("assets//my_work//t1.jpg", use_column_width=True)
        with col2:
            st.image("assets//my_work//t2.jpg", use_column_width=True)
        with col3:
            st.image("assets//my_work//t3.jpg", use_column_width=True)

    elif selected_tab == "Downloadables":
        col1, col2 = st.columns(2)
        with col1:
            st.image("assets//my_work//c1.png", use_column_width=True)
            st.page_link("https://i.pinimg.com/564x/4b/03/80/4b03801178387a30303e451f9621b99b.jpg", label="Download", icon="⬇")
        with col2:
            st.image("assets//my_work//c2.gif", use_column_width=True)
            st.page_link("https://i.pinimg.com/564x/4b/03/80/4b03801178387a30303e451f9621b99b.jpg", label="Download", icon="⬇")

    elif selected_tab == "Speedpaints":
        col1,col2=st.columns([1.5,0.87])
        with col1:
          video_file = open("assets//my_work//vid//1.mp4", "rb")
          video_bytes = video_file.read()
          st.video(video_bytes)
          
          video_file = open("assets//my_work//vid//2.mp4", "rb")
          video_bytes = video_file.read()
          st.video(video_bytes)
          
        with col2:    
          video_file = open("assets//my_work//vid//3.mp4", "rb")
          video_bytes = video_file.read()
          st.video(video_bytes)
          
          video_file = open("assets//my_work//vid//4.mp4", "rb")
          video_bytes = video_file.read()
          st.video(video_bytes)

elif selected_tab == "💻Portfolio 2":
    st.title("💻Coding Portfolio")
    left_column, right_column =  st.columns([0.5, 1.5])
    with left_column:
        st.image("assets//my_work//l1.png", width=250)
        st.image("assets//my_work//l2.png", width=250)
    with right_column:
        st.header("InfoHaven")
        st.write("""
            "InfoHaven -  Library Book Management System" is a comprehensive and efficient solution for managing library operations. 
            This system aims to automate and streamline various library functions, making it easier for both staff and patrons to 
            interact with the library's resources. Key functionalities include user account management, book search and retrieval, 
            real-time book availability updates, and fine management. The goal is to enhance the library experience, improve 
            operational efficiency, and provide users with a modern, intuitive platform for accessing library services. 
            """)
        st.write("""
            - **Frontend Stack**: HTML, CSS, JavaScript
            - **Backend Stack**: Django Framework (Python)
            """)
        st.progress(80,"")
        st.write("---")
        st.header("AttendEase Capstone Project")
        st.write("""
            "AttendEase" is a location-aware attendance tracking" is a mobile app for CIT-U, leveraging GPS to monitor faculty and student 
            attendance accurately. It simplifies attendance recording, enhances accountability, and offers real-time updates. 
            Faculty can take attendance with ease, while students check in effortlessly, all contributing to streamlined 
            attendance management at CITU.
            """)
        st.write("""
            - **Tech Stack**: Android Studio Kotlin for Mobile (Public Use), React.js for Web (Admin)
            - **Database**: Firebase - Firestore DB
            """)
        st.progress(70,"")

# --- MY CONTACTS
elif selected_tab == "📩Contact Me":
    st.title("📩Contact Me")
    left_column, right_column =  st.columns([1.8, 1.2])
    with left_column:
      st.subheader("Contact Form")
      contact_form = """
      <form action="https://formsubmit.co/paez.marie1019@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your Name" required><br>
        <input type="email" name="email" placeholder="Your Email" required><br>
        <textarea name="message" placeholder="Your Message"></textarea><br>
        <button type="submit">Send</button>
      </form>
      """
      st.markdown(contact_form, unsafe_allow_html=True)
      
      def local_css(file_name):
        with open(file_name) as f:
          st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
      local_css("assets//style//style.css")
      
    with right_column:
      st.subheader("Social Media")
      st.write("""
          - **Email**: paez.marie1019@gmail.com
          - **Facebook**: [Marie Antoinette](https://web.facebook.com/marionette1019/)
          - **Instagram**: [@ashen.dust](https://www.instagram.com/ashen.dust/)
      """)
    
