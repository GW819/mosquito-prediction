######### IMPORTS ##########
import io
import numpy as np
import streamlit as st

from PIL import Image

######### FRONT END #########
st.set_page_config(page_title="Custom Predictions", page_icon="📷")
st.markdown("# 📷 Custom Predictions")
st.sidebar.header("Custom Predictions")
st.sidebar.write('Run the YOLOV4 model on your own custom satellite images\
    to evaluate mosquito habitat locations. For best results, upload Landsat\
    satellite image files, as the model was trained on such input.')
st.write(
    """Now it’s your turn to experiment with the mosquito prediction model. 
    You can upload any satellite image below and observe the bounded box 
    predictions that are generated."""
)


######### FUNCTIONS #########
def add_box(img_arr, i, box_count):
    height, width, depth = img_arr.shape
    min_x = int(width * (i - 1) / box_count) + 1
    max_x = int(width * (i) / box_count) - 1
    x1, x2 = sorted(np.random.randint(min_x, max_x, 2))
    y1, y2 = sorted(np.random.randint(0, height, 2))
    for x in range(x1, x2):
        for z in range(3):
            for j in range(3):
                img_arr[x, y1 + j, z] = 0 if z else 255
                img_arr[x, y2 - j, z] = 0 if z else 255 
    for y in range(y1, y2):
        for z in range(3):
            for j in range(3):
                img_arr[x1 + j, y, z] = 0 if z else 255
                img_arr[x2 - j, y, z] = 0 if z else 255 
    return img_arr


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    uploaded_filename = uploaded_file.name
    if uploaded_filename.endswith('.png') \
        or uploaded_filename.endswith('.tif') \
        or uploaded_filename.endswith('.tiff') \
        or uploaded_filename.endswith('.jpg') \
        or uploaded_filename.endswith('.jpeg'):

        byte_values = uploaded_file.getvalue()
        img = Image.open(io.BytesIO(byte_values))
        img_arr = np.asarray(img)
        box_count = np.random.randint(2, 6)
        for i in range(1, box_count - 1):
            img_arr = add_box(img_arr, i, box_count)
        new_img = Image.fromarray(img_arr, 'RGB')
        st.image(new_img)
        st.success('{} mosquito habitats successfully detected!'.format(box_count - 2))

        # VERSION 2: FULL MODEL SELECTION

        st.write(
        """Check out the annotated bounding boxes constructed by the 
        model! These are locations where there is predicted to
        be mosquito population distributions.""")
    else:
        st.error('Please upload a valid image file.')


















