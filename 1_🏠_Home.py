
import streamlit as st

from PIL import Image

######### CONSTANTS #########
MAIN_FN = 'vis_images/main.jpg'
MAIN_MOD_FN = 'vis_images/main_annot.jpg'
DATA_RAW_FN = 'vis_images/data_raw.jpg'
DATA_MOD_FN = 'vis_images/data_mod.jpg'
PIPELINE_FN = 'vis_images/pipeline.png'


def run():
    st.set_page_config(
        page_title="Home",
        page_icon="🏠",
    )
    st.write("# 🏠 GeoMosquito AI 🦟")

    st.sidebar.markdown('## About')
    st.sidebar.success("GeoMosquito is a set of analyses to identify \
    	mosquitopopulations from satellite images using Machine\
    	Learning. The tool serves as a replication and advancement\
    	of the work on “CNN Mosquito Habitat Detection Research”\
    	by Sriram Elango and  Nandini Ramachandran.\n\
    	The tool explores the mosquito distribution datasets\
    	and runs models for mosquito prediction.\
    	The tool also allows users to submit custom satellite\
    	images of affected domains to evaluate\
    	for the presence of mosquito populations across the globe.\n\
    	The data is provided courtesy of the aforementioned work by\
    	Elango et. al. and can be accessed here. Note that the data in\
    	its current form is limited and that this tool is a work in\
    	progress.")

    images = [Image.open(MAIN_FN), Image.open(MAIN_MOD_FN)]
    col1, col2 = st.columns([1, 1])
    col1.markdown('##### Original')
    col2.markdown('##### Predicted Habitats')
    col1.image(images[0], use_column_width=True, caption=["Satellite image with no annotations of mosquito habitats."])
    col2.image(images[1], use_column_width=True, caption=["Satellite image with YOLOV4 model annotations of predicted mosquito habitat locations."])


    st.subheader('Development Process')
    st.write('The goal of GeoMosquito AI is to utilize satellite data to\
         predict mosquito habitat locations across the globe. This is done\
          in a 3 step process.')
    st.image(Image.open(PIPELINE_FN))

    st.subheader('Data')
    st.write('First, this begins with ground truth annotations of mosquito habitat locations.\
        This consists of several hundred satellite images in which bounding boxes are manually\
        annotated by an expert at locations with known likelihood of inhabiting mosquitos')

    images = [Image.open(DATA_RAW_FN), Image.open(DATA_MOD_FN)]
    col1, col2 = st.columns([1, 1])
    col1.markdown('##### Raw Image')
    col2.markdown('##### Ground Truth Annotations')
    col1.image(images[0], use_column_width=True, caption=["Raw satellite image"])
    col2.image(images[1], use_column_width=True, caption=["Satellite image with manual ground truth annotations"])

    st.subheader('Analysis')
    st.write('An exploratory data analysis is performed of the data to assess utility for a\
         Machine Learning model (see Exploratory Data Analysis page). Bodies of water and wetlands\
         are known breeding grounds for mosquitos, so the overlap in the classification of these\
         locales in the images is properly assessed.')

    st.subheader('Prediction')
    st.write('Custom predictions are thereby made on  any given satellite imagery (\
        see Custom Predictions Page)')




if __name__ == "__main__":
    run()





