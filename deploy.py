# DEPLOYMENT MODEL EGG GRADING AUTOMATION (FINAL PROJECT STARTUP CAMPUS AI BATCH 5)
# By: 404 Always Found 

# Import required modules 
import io
import torch
import streamlit as st
import torch, torchvision, time

from PIL import Image
from collections import Counter
from torchvision import transforms
from matplotlib import pyplot as plt


# Setting the Interface Color 
dark_mode_css = """
    <style>
        body {
            color: white;
            background-color: #1E1E1E;
        }
        .st-ba, .st-at, .st-dq, .st-dl, .st-dm, .st-jp, .st-ja, .st-bk {
            color: white;
        }
    </style>
"""
st.markdown(dark_mode_css, unsafe_allow_html=True)



# Define model architecture 
class VisionModel(torch.nn.Module):
    def __init__(self, model_selection : str, *args, **kwargs) -> None:
        super(VisionModel, self).__init__()
        self.model_selection = self.name = model_selection
        self.in_channels = 3

        if not self.model_selection.lower() in ["resnet", "densenet", "vit"]:
            raise ValueError("Please select the model: 'resnet', 'densenet', or 'vit'.")

        if self.model_selection == "resnet":
            self.model = torchvision.models.resnet18(pretrained=False)
            self.model.fc = torch.nn.Sequential(
              torch.nn.Linear(512, 256),
              torch.nn.ReLU(),
              torch.nn.Dropout(0.3),
              torch.nn.Linear(256, 3),        #
            )
        self.softmax = torch.nn.Softmax(dim=1)

    def forward(self, data, *args, **kwargs) -> torchvision.models:
        x = self.model(data)
        return self.softmax(x)
    


#Load Model
device = torch.device("cuda") if torch.cuda.is_available() else torch.device("cpu")
model = VisionModel('resnet').to(device)
loaded_model = torch.load("D:\MODEL-STARTUPCAMPUS\model-final-cadangan.pth",  map_location=torch.device('cpu'))
if 'module' in loaded_model:
    state_dict = loaded_model['module']
else:
    state_dict = loaded_model
model.load_state_dict(state_dict)

model.eval()



# Define  image transformation
mean = torch.tensor([0.6750, 0.6106, 0.5683])
std = torch.tensor([0.1580, 0.1903, 0.2257])
custom_transform = transforms.Compose([
    transforms.Resize((300, 300)),
    transforms.ToTensor(),
    torchvision.transforms.Normalize(mean=mean, std=std)
])


# Define Function for cropping image 
def crop_image(img_path, rows, cols):
    original_image = Image.open(img_path)
    width, height = original_image.size
    crop_width = width // cols
    crop_height = height // rows
    cropped_images = []
    for i in range(rows):
        for j in range(cols):
            left = j * crop_width
            top = i * crop_height
            right = (j + 1) * crop_width
            bottom = (i + 1) * crop_height
            cropped = original_image.crop((left, top, right, bottom))
            cropped_images.append(cropped)

    return cropped_images


# Define function to test model using the test image 
def test_image(image):
    image = custom_transform(image).unsqueeze(0)
    image = image.to(device)
    with torch.no_grad():
        output = model(image)
    return output


# Define code for create the sidebar 
st.sidebar.title(":gear: Options")
selected_option = st.sidebar.radio("Input Type.", ["Single Egg", "Multiple Eggs in Egg Tray"])
class_labels = ["Grade A", "Grade B", "Grade C"]

# Define code if user choose option 'single egg'
if selected_option == "Single Egg":  
    st.title(":egg: Egg Grading Automation:egg:")
    uploaded_file = st.file_uploader("Upload An Image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.markdown(
            """
            <style>
                button[title^=Exit]+div [data-testid=stImage]{
                    text-align: center;
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 100%;
                }
            </style>
            """, unsafe_allow_html=True
        )
        left_co, cent_co,last_co = st.columns(3)
        with cent_co:
            st.image(image, caption="Uploaded Image", width=200)
        with st.spinner("Classifying..."):
            result = test_image(image)
        result_list = result[0].tolist()
        max_prob_index = result_list.index(max(result_list))
        max_prob = result_list[max_prob_index]
        predicted_class = class_labels[max_prob_index]
        st.markdown(
            f'<div style="text-align:center;">'
            f'<p style="font-size: medium">Predicted Class: </p><p style="font-size: larger; font-weight: bold;">{predicted_class}</p>'
            f'</div>',
            unsafe_allow_html=True
        )

# Define code if user choose option 'Multiple Egg'
elif selected_option == "Multiple Eggs in Egg Tray":
    st.title(":egg: Egg Grading Automation:egg:")
    uploaded_file = st.file_uploader("Upload An Image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.markdown(
            """
            <style>
                button[title^=Exit]+div [data-testid=stImage]{
                    text-align: center;
                    display: block;
                    margin-left: auto;
                    margin-right: auto;
                    width: 100%;
                }
            </style>
            """, unsafe_allow_html=True
        )
        left_co, cent_co,last_co = st.columns(3)
        with cent_co:
            st.image(image, caption="Uploaded Image", width=200)
        row = st.number_input("Input the number of row", step=1, value=0, format="%d")
        col = st.number_input("Input the number of columns", step=1, value=0, format="%d")
        if st.button("Classify"):
            cropped_image = crop_image(uploaded_file,row,col)
            with st.spinner("Classifying... (This process requires additional time as it utilizes the CPU)"):
                PRED_CLASS = []
                fig, axes = plt.subplots(row, col, figsize=(20,20))
                for i in range(row * col):
                    if row != 1:
                        row_idx = i // col
                        col_idx = i % col
                        axes[row_idx, col_idx].imshow(cropped_image[i])
                        axes[row_idx, col_idx].axis("off")
                    elif row == 1:
                        col_idx = i
                        axes[col_idx].imshow(cropped_image[i])
                        axes[col_idx].axis("off")
                    result = test_image(cropped_image[i])
                    result_list = result[0].tolist()
                    max_prob_index = result_list.index(max(result_list))
                    max_prob = result_list[max_prob_index]
                    predicted_class = class_labels[max_prob_index]
                    if row != 1:
                        axes[row_idx, col_idx].set_title(predicted_class, fontsize=36)
                    elif row == 1:
                        axes[col_idx].set_title(predicted_class, fontsize=36)
                    PRED_CLASS.append(predicted_class)

                # st.markdown(":magic_wand:<h5> Result</h5>", unsafe_allow_html=True)
                st.subheader(":magic_wand: Result :magic_wand:")
                plt.tight_layout()
                st.pyplot(fig)
                class_counter = Counter(PRED_CLASS)
                st.write("The quantity of eggs per grade : ")
                for item, count in class_counter.items():
                    st.write((f":egg: {item} : {count} eggs"))
            