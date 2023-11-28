# Egg Grading Automation: Quality Classification Based on its External Property (Shell Color) Through Transfer Learning Using ResNet-18

## Project Description
Please describe your Startup Campus final project here. You may should your <b>model architecture</b> in JPEG or GIF.

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
| | |
| --- | --- |
| GPU | Tesla T4 |
| ROM | 166.77 GB, used: 26.89 GB |
| RAM | 12.68 GB, used: 1.54 GB |
| OS  | microsoft windows v10.0.2 |

## Dataset
The dataset used consists of images of 'Commercial Chicken Eggs' collected manually using a smartphone camera. The images were captured at a distance of approximately 10cm with a plain white egg background. The dataset comprises 600 egg images categorized into three quality classes: Grade A, Grade B, and Grade C. Below are examples of egg images, arranged from left to right representing Grade A, Grade B, and Grade C, respectively. 

![WhatsApp Image 2023-11-27 at 11 17 35](https://github.com/putrinahampun/final-project-scAI5/assets/72849694/671346e3-fa00-4274-abac-a5368a2b90ab)


Link: [Access our dataset through this Link](https://drive.google.com/drive/folders/1--F2ivjU88cwfi_5Xko7VKb_V1QuAug7?usp=sharing)


## Results
### Model Performance
In this task, several experiments and modifications were conducted on different versions of the ResNet architecture. The best results were achieved using the ResNet-18 architecture with additional Linear, ReLU, and Dropout layers. The optimal model was obtained by setting the parameters to batch_size = 64, learning_rate = 0.0001, and epoch = 100, resulting in an accuracy of 91%.

#### 1. Metrics

| model | epoch | learning_rate | batch_size | optimizer | val_loss | val_precision | val_recall | ... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ResNet-50 | 20 |  0.0001 | 32 | Adam | 0.093 | 88.34% | 84.15% | ... |
| ResNet-18 | 50 | 0.001 | 64 | Adam | 0.041 | 90.19% | 87.55% | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | 

#### 2. Ablation Study
Any improvements or modifications of your base model, should be summarized in this table. Feel free to adjust the columns in the table below.

| model | layer_A | layer_B | layer_C | ... | top1_acc | top5_acc |
| --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | Conv(3x3, 64) x2 | Conv(3x3, 512) x3 | Conv(1x1, 2048) x3 | ... | 77.43% | 80.08% |
| vit_b_16 | Conv(3x3, 32) x3 | Conv(3x3, 128) x3 | Conv(1x1, 1028) x2 | ... | 72.11% | 76.84% |
| ... | ... | ... | ... | ... | ... | ... |

#### 3. Training/Validation Curve
 ![Screenshot 2023-11-25 121155](https://github.com/putrinahampun/final-project-scAI5/assets/72849694/19f2a508-8bdb-4937-8269-10348e79c410)

### Testing
Show some implementations (demos) of this model. Show **at least 10 images** of how your model performs on the testing data.

### Deployment (Optional)
Describe and show how you deploy this project (e.g., using Streamlit or Flask), if any.

## Supporting Documents
### Presentation Deck
- Link: 

### Business Model Canvas
Provide a screenshot of your Business Model Canvas (BMC). Give some explanations, if necessary.

### Short Video
Provide a link to your short video, that should includes the project background and how it works.
- Link: https://...

## References
Provide all links that support this final project, i.e., papers, GitHub repositories, websites, etc.
- Link: https://...
- Link: https://...
- Link: https://...

## Additional Comments
Provide your team's additional comments or final remarks for this project. For example,
1. ...
2. ...
3. ...

## How to Cite
If you find this project useful, we'd grateful if you cite this repository:
```
@article{
...
}
```

## License
For academic and non-commercial use only.

## Acknowledgement
This project entitled <b>"YOUR PROJECT TITLE HERE"</b> is supported and funded by Startup Campus Indonesia and Indonesian Ministry of Education and Culture through the "**Kampus Merdeka: Magang dan Studi Independen Bersertifikasi (MSIB)**" program.
