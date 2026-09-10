import streamlit as st
from blood_donor_views import BloodDonorManager

donor_instance = BloodDonorManager()

tab1,tab2 = st.tabs(['ADD','VIEW'])

with tab1:
    st.title('Add Blood Donor')
    name=st.text_input('Enter the donor name :')
    blood_group = st.text_input('Enter the blood group :')
    mobile = st.text_input('Enter the phone number :')
    city = st.text_input('Enter the city :')
    last_donation = st.text_input('Enter last donation :')
    if st.button('Add New Blood Donor'):
        donor_instance.post(name=name,blood_group=blood_group,phone=mobile,city=city,blood_donation=last_donation)
        st.success('Donor Added Successfully...')
with tab2:
    st.title('View Blood Donor Details')