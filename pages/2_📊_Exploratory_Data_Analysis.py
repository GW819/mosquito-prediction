
######### IMPORTS ##########
import os
import pandas as pd
import altair as alt
import streamlit as st

from PIL import Image
from collections import Counter

######### CONSTANTS #########
BASE_DIR = 'data'
H1_FN = 'vis_images/H1.jpg'
H2_FN = 'vis_images/H2.jpg'
H3_FN = 'vis_images/H3.jpg'
H4_FN = 'vis_images/H4.jpg'
H5_FN = 'vis_images/H5.jpg'
H6_FN = 'vis_images/H6.jpg'

######### FUNCTIONS #########
@st.cache
def read_in_data():
    pass

def get_line_count(fn):
    return sum(1 for line in open(fn))

train_files = os.listdir(os.path.join(BASE_DIR, 'train'))
train_image_fns = [x for x in train_files if x.endswith('.jpg')]
train_annot_fns = [x for x in train_files if x.endswith('.txt')]
train_annot_line_counts = {x:get_line_count(os.path.join(BASE_DIR, 'train', x)) for x in train_annot_fns}
train_sample_count = len(train_image_fns)

valid_files = os.listdir(os.path.join(BASE_DIR, 'valid'))
valid_image_fns = [x for x in valid_files if x.endswith('.jpg')]
valid_annot_fns = [x for x in valid_files if x.endswith('.txt')]
valid_annot_line_counts = {x:get_line_count(os.path.join(BASE_DIR, 'valid', x)) for x in valid_annot_fns}
valid_sample_count = len(valid_image_fns)

test_files = os.listdir(os.path.join(BASE_DIR, 'test'))
test_image_fns = [x for x in test_files if x.endswith('.jpg')]
test_annot_fns = [x for x in test_files if x.endswith('.txt')]
test_annot_line_counts = {x:get_line_count(os.path.join(BASE_DIR, 'test', x)) for x in test_annot_fns}
test_sample_count = len(test_image_fns)

all_line_counts = list(train_annot_line_counts.values())\
                    + list(valid_annot_line_counts.values())\
                    + list(test_annot_line_counts.values())
habitat_frequencies = dict(Counter(all_line_counts))
train_frequencies = dict(Counter(list(train_annot_line_counts.values())))
valid_frequencies = dict(Counter(list(valid_annot_line_counts.values())))
test_frequencies = dict(Counter(list(test_annot_line_counts.values())))

######### FRONT END #########
st.set_page_config(page_title="Exploratory Data Analysis", page_icon="📊")
st.markdown("# 📊 Exploratory Data Analysis")
st.sidebar.header("Exploratory Data Analysis")
st.write(
    """Here we explore the input dataset in a bit more detail.
    First we take a look at the distribution of the data among the 
    training/valid/testing sets. Then, we explore the distribution
    of mosquitos across the different satellite images of the input."""
)

st.subheader('Train/Valid/Test Sets')
st.write('We first take a look at the distribution of samples among the\
    different test sets. Ensuring a well-balanced distribution in which\
    the majority of samples belongs to the training set will yield the \
    best evaluation results.')
source = pd.DataFrame({
    'Number of Samples': [train_sample_count, valid_sample_count, test_sample_count],
    'Dataset': ['Train', 'Validation', 'Test']
 })
bar_chart = alt.Chart(source).mark_bar().encode(
    y='Number of Samples:Q',
    x='Dataset:O',
)
st.altair_chart(bar_chart, use_container_width=True)


st.subheader('Data Visualization')
st.write('Next, we take a look at the different input images and the\
     existing bounding box manual annotations of mosquito populations.')
col1, col2 = st.columns([1, 1])
with col1:
   st.image(Image.open(H1_FN), caption='1 possible mosquito habitat')
   st.image(Image.open(H3_FN), caption='3 possible mosquito habitats')
   st.image(Image.open(H5_FN), caption='4 possible mosquito habitats')

with col2:
   st.image(Image.open(H2_FN), caption='2 possible mosquito habitats')
   st.image(Image.open(H4_FN), caption='4 possible mosquito habitats')
   st.image(Image.open(H6_FN), caption='6 possible mosquito habitats')


st.subheader('Mosquito Population Frequencies')
st.write('Now we will look at the count of the possible mosquito habitats across\
     the input data and ensure a balanced representation among all the\
     datasets as well is within datasets.')

# TODO: ADD SELECTION ON SIDE BAR TO CHANGE PLOT CONTENTS BELOW
st.sidebar.write('Below you can select which set of the data you would like\
    to be depicted in the Mosquito Habitat Frequencies Plot.')
selectbox = st.sidebar.selectbox(
    "Dataset",
    ("All", "Train", "Valid", "Test")
)
if selectbox == 'All':
    frequencies = train_frequencies
if selectbox == 'Train':
    frequencies = valid_frequencies
elif selectbox == 'Test':
    frequencies = test_frequencies
else:
    frequencies = habitat_frequencies
source = pd.DataFrame({
    'Number of Samples': frequencies.values(),
    'Number of Possible Habitats': frequencies.keys()
 })
bar_chart = alt.Chart(source).mark_bar().encode(
    y='Number of Samples:Q',
    x='Number of Possible Habitats:O',
)
st.altair_chart(bar_chart, use_container_width=True)

st.write('As we can see, the distribution of the mosquito habitats among the train,\
     valid, and test sets is quite wide. I am actively working on obtaining more data in\
     order to create a more balanced data distribution for this problem.')







