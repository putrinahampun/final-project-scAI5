# 🥚 Egg Grading Automation: Quality Classification Based on its External Property (Shell Color) Using ResNet-18 🥚

## Project Description
🖼️ **Background :**

Egg is a primary source of protein and possess high nutritional value. The relatively low cost of eggs makes them the fourth most consumed commodity among the Indonesian population (BPS, 2021). Eggs vary in quality and are categorized into three grades according to the Indonesian National Standard (SNI): Grade A, B, and C. One observable factor used to classify egg quality is the "egg color". However, in some cases, such as with egg vendors, egg classification is still done manually, leading to time-consuming processes. Additionally, consumers often rely solely on egg size when making purchases, despite the fact that egg size may not necessarily reflect egg quality.

🎯 **Target:** 

This project aims to develop a system that can automatically grade eggs into three quality categories, namely Grade A, B, and C, in accordance with the Indonesian National Standard (SNI) based on egg color.

![arsitektur_resnet18](https://github.com/putrinahampun/final-project-scAI5/assets/72849694/9650c7d6-770c-4a08-b1de-f776622dd992)

## Contributor

| Full Name                   | Affiliation                          | Email                     | LinkedIn                                                          | Role        |
|-----------------------------|--------------------------------------|---------------------------|--------------------------------------------------------------     |-------------|
| Ridhatullah Akmalurrizal F. | Universitas Padjadjaran              | ridhatullah216@gmail.com  |[link](https://www.linkedin.com/in/ridhatullahaf/)                 | Team Lead   |
| Ernawati Prahesta           | Institut Teknologi Telkom Purwokerto | ernawatiphss@gmail.com    |[link](http://www.linkedin.com/in/ernawatiprahesta)                | Team Member |
| Ivander Marvin A.           | Universitas Sebelas Maret            | ivandermarvin09@gmail.com |[link](https://www.linkedin.com/in/ivander-marvin-68aa73220/)      | Team Member |
| Putri Yanti N.              | Universitas Sumatera Utara           | putrinahampun26@gmail.com |[link](https://www.linkedin.com/in/putriyantinahampun/)            | Team Member |
| Fathia Riska A.             | Universitas Bina Sarana Informatika  | fathiariskaamll@gmail.com |[link](https://www.linkedin.com/in/fathia-riska-amalia-602b52249/) | Team Member |
| Khafizh Khairy              | Universitas Riau                     | khafizhkhairy@gmail.com   |[link](https://www.linkedin.com/in/khafizh-khairy-5bb543262/)      | Team Member |
| Rika Sahriana               | Startup Campus, AI Track             | rikasahriana28@gmail.com  |[link](https://www.linkedin.com/in/rikasahriana/)                  | Supervisor  |

## Setup
### Prerequisite Packages (Dependencies)
- torch == 2.1.0+cu118
- torchvision == 0.16.0+cu118
- seaborn == 0.12.2
- numpy == 1.23.5
- tqdm == 4.66.1
- sklearn == 1.2.2
- matplotlib == 3.7.1
- python3 == 3.10.12 

### Environment
💻 Colab's Environment:
| | |
|-----|----------|
| GPU | Tesla T4 |
| ROM | 166.77 GB, used: 26.89 GB |
| RAM | 12.68 GB, used: 1.54 GB |
| OS  | microsoft windows v10.0.2 |

## Dataset
The dataset used consists of images of 'Telur Ayam Ras' collected manually using a smartphone camera.
The collected dataset comprises 600 egg images, with each quality category containing 200 eggs (Grade A, B, and C).

Egg Color Criteria:
- Grade A: Brown
- Grade B: Light Brown
- Grade C: Off-White Brown

Link: [Access our dataset through this Link](https://drive.google.com/drive/folders/1--F2ivjU88cwfi_5Xko7VKb_V1QuAug7?usp=sharing)

![WhatsApp Image 2023-11-27 at 11 17 35](https://github.com/putrinahampun/final-project-scAI5/assets/72849694/671346e3-fa00-4274-abac-a5368a2b90ab)


## Results
### Model Performance
In this task, some experiments and modifications were conducted on different versions of the ResNet architecture. The best results were achieved using the ResNet-18 architecture with additional Linear, ReLU, and Dropout layers. The optimal model was obtained by setting the parameters to **batch_size = 64, learning_rate = 0.0001, and epoch = 100**, resulting in an accuracy of **91%**.

#### 1. Metrics

| model | epoch | learning_rate | batch_size | optimizer | val_loss | val_precision | val_recall |
| --- | --- | --- | --- | --- | --- | --- | --- | 
| ResNet-50 | 50 |  0.0005 | 32 | Adam | 0.568 | 78.18% | 70% | 
| ResNet-50 | 50 | 0.0005 | 64 | Adam | 0.572 | 88.07% | 86.6% |
| ResNet-18 | 50 | 0.001 | 32 | Adam | 0.567 | 83.76% | 68.33% | 
| ResNet-18 | 100 | 0.001 | 32 | Adam | 0.559 | 86.48% | 86.67% | 
| ResNet-18 | 50 | 0.0001 | 64 | Adam | 0.557 | 90.24% | 90% | 
| **ResNet-18** | **100** | **0.0001** | **64** | **Adam** | **0.554** | **93%** | **91.67%** |

#### 2. Training/Validation Curve
![Screenshot 2023-11-25 121155](https://github.com/putrinahampun/final-project-scAI5/assets/72849694/19f2a508-8bdb-4937-8269-10348e79c410)

### Testing
Demo for testing some images:

Dataset (10 images) saved here: [dataset-10-testing](https://drive.google.com/drive/folders/1h-1Jk1m0Bd6O3e9RFSYZgwWaos7KVX0i?usp=sharing)

![ezgif com-video-to-gif](https://github.com/putrinahampun/final-project-scAI5/assets/72849694/2f77b460-e0bf-4806-815c-6a33bce7682e)

### Deployment
📑 Library Used: Streamlit.

💻 IDE: Visual Studio Code.

⚪ Classification Options : **Singular Egg and Multiple Eggs in EggTray**.

📔 Procedures:
- Identify your object (is it single egg or multiple egg?). Then, select the options provided (Single Egg / Multiple Egg in EggTray)
- Upload your image.
- For 'Single Egg' image, the model will output the prediction results as soon as the image is uploaded.
- For 'Multiple Egg in EggTray' image, you must first input the 'row' and 'column' values of the egg image to help the model perform the 'auto-blocking' process. After that, the model will return the prediction result.
- Auto-blocking is used to separate each egg image from the eggtray image, so the model can classify the eggs. 

## Supporting Documents
### Presentation Deck
- Link: 

### Business Model Canvas
![BMC TIM D_page-0001](https://github.com/putrinahampun/final-project-scAI5/assets/72849694/0da309db-2374-4e0e-ad7e-edfb87ad90ca)
![BMC TIM D_page-0002](https://github.com/putrinahampun/final-project-scAI5/assets/72849694/5f6456ae-680f-438f-a165-7f9d43ea2384)

### Short Video
Provide a link to your short video, that should includes the project background and how it works.
- Link: https://...

## References
Provide all links that support this final project, i.e., papers, GitHub repositories, websites, etc.
- Link: https://towardsdatascience.com/understanding-and-visualizing-resnets-442284831be8 
- Link: https://medium.com/@freshtechyy/a-detailed-introduction-to-resnet-and-its-implementation-in-pytorch-744b13c8074a 
- Link: https://pytorch.org/hub/pytorch_vision_resnet/
- Link: https://pytorch.org/vision/main/models/generated/torchvision.models.resnet18.html
- Link: https://streamlit.io/ 

## Additional Comments
📌 **Scope of The Study** 

    1. EGA is designed for egg distributors who still manually categorize egg quality.
    2. EGA can classify individual eggs and multiple eggs in an egg tray.
    3. Images of 'multiple eggs in egg tray' are captured from the top.
    4. Uploaded egg images are clear and well-visible.
    5. 'Multiple egg' images should have an egg tray background.
    6. The size of the column and row values in the 'multiple eggs in egg tray' 
    7. Classification is greater than or equal to 1.
    8. Deployment results are currently accessed locally.

📑**Future Work** 

    1. Enhance the quality and diversity of the dataset.
    2. Enable EGA to perform real-time classification.
    3. Make deployment results accessible online (deployable on devices such as Android).
    4. Experiment with models other than ResNet to improve application performance.

## License
For academic and non-commercial use only.

## Acknowledgement
This project entitled <b>"Egg Grading Automation: Quality Classification Based on its External Property (Shell Color) Using ResNet-18"</b> is supported and funded by Startup Campus Indonesia and Indonesian Ministry of Education and Culture through the "**Kampus Merdeka: Magang dan Studi Independen Bersertifikasi (MSIB)**" program.
