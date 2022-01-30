# COVID-19 ASSISTANT
Chatbot using Covid-19
## *1. Output :zipper_mouth_face:*
Recorded Demo of the project = https://youtu.be/OpU8z3stYUM
The codes and folders are here = https://drive.google.com/drive/folders/1UDBGfWFErzlfhypz0jkqydEL-YjK0VSR

## *2. Description :thinking:*
  - We created a chatbot using RASA.<br/>
  - We first modified the nlu.yml,stories.yml,domain.yml to set the customized intents for the chatbot to identify and answer. <br/>
  - Internally the input given by users are converted to vectors using Bag Of Words amd Count Vectoriser.<br/>
  - According to the vectors of the files as mentioned above(intent,stories,etc), the distances are calculated of the Input vectors.<br/> 
  - The closest vectors are then chosen by model and the intent is understood.<br/>
  - According tp intent, the response(eg. utter_corona_symptoms from domain.yml) is displayed.<br/>
  - We also used api(https://data.covid19india.org/data.json) for the data collection live covid cases.<br/>
  - Accordingly new intent,story and domain was added in the respective files.</br>
  - In actions.py the data from api was collected in json format and the dictionary elements were matched with the input variable(taken from user).<br/>
  - If there is a match the respective data is shown, otherwise error correction message is shown.<br/>
 ## *3. Used*
 ![Logo](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
 - RASA
 ## *4. IDE*
 ![Logo](https://img.shields.io/badge/Visual_Studio-5C2D91?style=for-the-badge&logo=visual%20studio&logoColor=white)
 ## *5. Future Improvements :raised_eyebrow:*
 Looking to improve the output of chatbot with more intent and data.
 ## *6. Contributers :nerd_face:*
  - Ayush Roy<br/>
  - Ritwick Halder<br/>
  - Arkaprava Acharya<br/>
