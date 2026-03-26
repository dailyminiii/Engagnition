## 📊 About Engagnition

![Data fig Teaser](https://github.com/dailyminiii/Engagnition/assets/79134282/684613e8-3ea7-4e85-be81-48f0dd13a24d)

Engagement plays a critical role in supporting the cognitive and motor development of children with autism spectrum disorder (ASD). Prior work has shown that engaging technologies involving physical activity and interactive stimuli can help improve engagement and reduce stereotyped behaviors. In particular, systems that combine tangible and intangible robot agents may foster engagement in children with developmental disorders. When such systems are integrated with AI, they can enable engagement prediction and timely intervention, potentially helping maintain high levels of engagement over time.

However, the development of engagement prediction models has been limited by the lack of publicly available datasets for children with ASD. To address this gap, we present **Engagnition**, a multimodal dataset for engagement recognition in children with ASD (\(N = 57\)), collected using a self-developed serious game, **Defeat the Monster**, designed to support recognition and classification abilities. The dataset includes physiological and behavioral responses, along with expert annotations based on a ternary engagement scale used as ground truth. For technical validation, we report engagement distributions, intervention status by participant, and the signal-to-noise ratio (SNR) of physiological signals.

---

## 📦 Dataset Availability

To support reproducibility and further research, the **Engagnition dataset** is publicly available at:

🔗 https://doi.org/10.6084/m9.figshare.c.6879628

The repository includes the dataset and associated materials necessary for research on engagement recognition, adaptive intervention, and multimodal analysis in developmental contexts.

---

## 📊 Overview

Welcome to the GitHub repository for our Developmental Disabilities and Physical Activity Series Game project. 🎉  
In this project, we designed and developed a serious game centered around physical activity, specifically tailored for children with developmental disabilities. Through this effort, we collected valuable multimodal data to better understand how physically interactive games can positively influence the well-being and development of children facing developmental challenges.

---

## 📊 Project Description

Our goal is to create an interactive environment in which children with developmental disabilities can participate in physical activities in an engaging and supportive way. We believe that gamified physical exercise can foster engagement while promoting essential cognitive and motor skills through playful interaction.

---

## 📊 Key Features

- Specifically designed for engagement recognition in children with developmental disabilities (\(N = 57\))
- Incorporates both physiological and behavioral responses for comprehensive analysis
- Includes expert annotations based on a ternary scale as engagement ground truth
- Supports research on engagement recognition, adaptive intervention, and human-AI interaction

---

## 📊 Data Collection Environment for the Engagnition Dataset

The Engagnition dataset was collected at a physical fitness center specifically designed for children with developmental disabilities.

![Data fig Setup Condition](https://github.com/dailyminiii/Engagnition/assets/79134282/09239254-4da0-4d7a-9360-68371c4dde9b)

### Data Sources

- **E4 Wristband**  
  A wearable biometric sensor used to collect physiological signals, including:
  - Accelerometer (ACC)
  - Galvanic Skin Response (GSR)
  - Skin Temperature (TEMP)

- **Unity-Based Game**  
  Participants interacted with a custom-developed serious game built in Unity. The system recorded:
  - Performance annotations
  - Session elapsed times
  - Game interaction logs

- **Behavioral Annotations**
  - Engagement annotations
  - Gaze fixation annotations

- **Subjective Questionnaires**
  - SUS
  - NASA-TLX

![Data fig Monster and Task](https://github.com/dailyminiii/Engagnition/assets/79134282/7e69e7b4-a4bc-40c3-90ef-0e799ff3acc6)

---

## 📊 Experimental Conditions

Data collection was conducted under three different conditions to capture a broad range of engagement states:

- **Baseline**  
  Captures foundational physiological and behavioral measures without additional task demand or external stimulus.

- **Physical High Demand**  
  Captures responses when participants were exposed to tasks requiring high physical engagement.

- **Physical Low Demand**  
  Captures responses under tasks requiring relatively low levels of physical activity or engagement.

---

## 📊 Engagement Levels

Engagement during the sessions was categorized into three levels:

![Data fig Engagement Example](https://github.com/dailyminiii/Engagnition/assets/79134282/81afebbb-4545-4d30-b83b-f6008adc4732)

- **0**: Not engaged at all
- **1**: Moderately engaged
- **2**: Fully engaged

These labels were determined in collaboration with experts specializing in developmental disabilities to ensure informed and reliable engagement annotation.

---

## 🔒 Consent

All participants, or their legal guardians, provided explicit informed consent for the data to be publicly released and used for research purposes.

---

## 📑 Citation

If you use this dataset in your research, please cite the repository below:

```bibtex
@dataset{engagnition_dataset,
  author       = {Minwoo Seong and colleagues},
  title        = {Engagnition: A Multimodal Dataset for Engagement Recognition of Children with ASD},
  year         = {2023},
  publisher    = {figshare},
  doi          = {10.6084/m9.figshare.c.6879628},
  url          = {https://doi.org/10.6084/m9.figshare.c.6879628}
}
```

## Contact
Email: kimwon30 AT gm.gist.ac.kr, seongminwoo AT gm.gist.ac.kr
