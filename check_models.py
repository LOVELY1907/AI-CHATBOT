import google.generativeai as genai

genai.configure(api_key="AIzaSyBCNM_YgkZLw8T-z9rWb7N_Fs1W97RaBm4")

for model in genai.list_models():
    print(model.name)
