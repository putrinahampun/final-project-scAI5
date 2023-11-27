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
| Khafizh Khairy              | Universitas Riau                     | ...                       | ...                                                               | Team Member |
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
The dataset used consists images of 'Telur Ayam Ras' collected manually using a smartphone camera. The collected dataset comprises 600 egg images, with each quality category containing 200 eggs (Grade A, B, and C).

Link: [drive_egg_dataset](https://drive.google.com/drive/folders/1--F2ivjU88cwfi_5Xko7VKb_V1QuAug7?usp=sharing)
(Grade A)
![IMG_2085](https://github.com/putrinahampun/final-project-scAI5/assets/72849694/64240a87-6208-4266-9f9e-dcb7a53e7369) 

## Results
### Model Performance
Describe all results found in your final project experiments, including hyperparameters tuning and architecture modification performances. Put it into table format. Please show pictures (of model accuracy, loss, etc.) for more clarity.

#### 1. Metrics
Inform your model validation performances, as follows:
- For classification tasks, use **Precision and Recall**.
- For object detection tasks, use **Precision and Recall**. Additionaly, you may also use **Intersection over Union (IoU)**.
- For image retrieval tasks, use **Precision and Recall**.
- For optical character recognition (OCR) tasks, use **Word Error Rate (WER) and Character Error Rate (CER)**.
- For adversarial-based generative tasks, use **Peak Signal-to-Noise Ratio (PNSR)**. Additionally, for specific GAN tasks,
  - For single-image super resolution (SISR) tasks, use **Structural Similarity Index Measure (SSIM)**.
  - For conditional image-to-image translation tasks (e.g., Pix2Pix), use **Inception Score**.

Feel free to adjust the columns in the table below.

| model | epoch | learning_rate | batch_size | optimizer | val_loss | val_precision | val_recall | ... |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | 1000 |  0.0001 | 32 | Adam | 0.093 | 88.34% | 84.15% | ... |
| vit_l_32 | 2500 | 0.00001 | 128 | SGD | 0.041 | 90.19% | 87.55% | ... |
| ... | ... | ... | ... | ... | ... | ... | ... | ... | 

#### 2. Ablation Study
Any improvements or modifications of your base model, should be summarized in this table. Feel free to adjust the columns in the table below.

| model | layer_A | layer_B | layer_C | ... | top1_acc | top5_acc |
| --- | --- | --- | --- | --- | --- | --- |
| vit_b_16 | Conv(3x3, 64) x2 | Conv(3x3, 512) x3 | Conv(1x1, 2048) x3 | ... | 77.43% | 80.08% |
| vit_b_16 | Conv(3x3, 32) x3 | Conv(3x3, 128) x3 | Conv(1x1, 1028) x2 | ... | 72.11% | 76.84% |
| ... | ... | ... | ... | ... | ... | ... |

#### 3. Training/Validation Curve
Insert an image regarding your training and evaluation performances (especially their losses). The aim is to assess whether your model is fit, overfit, or underfit.
 
### Testing
Show some implementations (demos) of this model. Show **at least 10 images** of how your model performs on the testing data.

### Deployment (Optional)
Describe and show how you deploy this project (e.g., using Streamlit or Flask), if any.

## Supporting Documents
### Presentation Deck
- Link: https://...

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
