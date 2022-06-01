import streamlit as st
from PIL import Image
import numpy as np
import cv2 #computer vision 


def convertto_watercolorsketch(inp_img):
    st.write('1')
    dst = cv2.edgePreservingFilter(inp_img, flags=2, sigma_s=50, sigma_r=0.8)
    st.write('3')
    dst_water_color = cv2.stylization(dst, sigma_s=100, sigma_r=0.5)
    return(dst_water_color)

def load_image(image_file):
	img = Image.open(image_file)
	return img

def main():       
    hide_streamlit_style = """
                <style>
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True) 
    st.title('WEB APPLICATION TO CONVERT IMAGE TO SKETCH')
    st.write("This is an application developed for converting your ***image*** to a ***sketch***")
    st.subheader("Please Upload your image")
    image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
    if image_file is not None:
              # To View Uploaded Image
			  st.image(load_image(image_file),width=250)
              
    if image_file is not None:
        option = st.selectbox(
     'How would you like to convert the image',
     ('Convert to water color sketch', 'Convert to pencil sketch', 'Convert to color pencil sketch'))
        if option == 'Convert to water color sketch':
            image = Image.open(image_file)
            final_sketch = convertto_watercolorsketch(np.array(image))
            im_pil = Image.fromarray(final_sketch)
            st.image(im_pil,width=250)


if __name__=='__main__': 
    main()