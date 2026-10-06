
import streamlit as st
import requests


API_URL = "http://127.0.0.1:8000"


st.set_page_config(
    page_title="Student Management",
    page_icon="🎓"
)

st.title("🎓 Student Management System")


# =========================
# ADD STUDENT
# =========================

st.header("Add Student")

roll_no = st.number_input(
    "Roll Number",
    min_value=1,
    step=1
)

name = st.text_input("Name")

email = st.text_input("Email")

branch = st.text_input("Branch")


if st.button("Add Student"):

    data = {
        "roll_no": roll_no,
        "name": name,
        "email": email,
        "branch": branch
    }

    try:

        response = requests.post(
            f"{API_URL}/students",
            json=data
        )

        if response.status_code == 200:

            st.success("Student added successfully! 🎉")

        else:

            st.error(
                f"Error: {response.text}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "FastAPI server is not running."
        )


# =========================
# GET STUDENTS
# =========================

st.divider()

st.header("All Students")


if st.button("Load Students"):

    try:

        response = requests.get(
            f"{API_URL}/students"
        )

        if response.status_code == 200:

            students = response.json()

            if students:

                st.dataframe(
                    students,
                    use_container_width=True
                )

            else:

                st.info("No students found.")

        else:

            st.error(
                f"Error: {response.text}"
            )

    except requests.exceptions.ConnectionError:

        st.error(
            "FastAPI server is not running."
        )
