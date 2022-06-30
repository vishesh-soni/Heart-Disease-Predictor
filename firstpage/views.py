import pickle
from tkinter.messagebox import NO
from django.shortcuts import render
import pandas as pd
from requests import put


def predict(request):
    return render(request,'predict.html')

def output(request):
    Smoking = request.POST.get('Smoking')
    AlcoholDrinking = request.POST.get('AlcoholDrinking')
    Stroke = request.POST.get('Stroke')
    DiffWalking = request.POST.get('DiffWalking')
    Diabetic = request.POST.get('Diabetic')
    PhysicalActivity = request.POST.get('PhysicalActivity')
    BMI= int(request.POST.get('BMI'))
    Sex = request.POST.get('Sex')
    Asthma = request.POST.get('Asthma')
    KidneyDisease = request.POST.get('KidneyDisease')
    SkinCancer = request.POST.get('SkinCancer')
    Race = request.POST.get('Race')
    PhysicalHealth = int(request.POST.get('PhysicalHealth'))
    SleepTime = int(request.POST.get('SleepTime'))
    MentalHealth = int(request.POST.get('MentalHealth'))
    Age = int(request.POST.get('Age'))
    GenHealth = request.POST.get('GenHealth')

    
    df = pd.DataFrame([BMI],columns=["BMI"])
    df['Smoking'] = Smoking
    df['AlcoholDrinking'] = AlcoholDrinking
    df['Stroke'] = Stroke
    df['PhysicalActivity'] = PhysicalActivity
    df['PhysicalHealth'] = PhysicalHealth
    df['MentalHealth'] = MentalHealth
    df['DiffWalking'] = DiffWalking
    df['Sex'] = Sex
    df['AgeCategory'] = Age
    df['Race'] = Race
    df['Diabetic'] = Diabetic
    df['GenHealth'] = GenHealth
    df['SleepTime'] = SleepTime
    df['Asthma'] = Asthma
    df['KidneyDisease'] = KidneyDisease
    df['SkinCancer'] = SkinCancer

    binary = {"No":0,"Yes":1}
    sex = {"Female":0,"Male":1}
    GenHealth = {'Very good':0, 'Fair':1, 'Good':2, 'Poor':3, 'Excellent':4}
    race = {'White':0, 'Black':1, 'Asian':2, 'American Indian/Alaskan Native':3,
        'Other':4, 'Hispanic':5}

    


    col = ["Smoking","AlcoholDrinking","Stroke","DiffWalking","Diabetic","PhysicalActivity","Asthma","KidneyDisease","SkinCancer"]
    for i in col:
        df[i] = df[i].replace(binary)
    print(df['Sex'])
    df['Sex']=df['Sex'].replace(sex)
    df['GenHealth']=df['GenHealth'].replace(GenHealth)
    df['Race'] = df['Race'].replace(race)
    
    # context = {'df':df}

    filename = r"./models/finalized_model.sav"
    # pickle.dump(xgbcl, open(filename,'wb'))

    loaded_model = pickle.load(open(filename, 'rb'))
    test = loaded_model.predict(df)

    out = None
    if test == '0':
        out = "don't have Heart Disease"
    
    elif test==1:
        out = "have Heart Disease"
    
    else:
        out = "Report have some issue will again calculate the report"
    
    context = {"Smoking":Smoking,"AlcoholDrinking":AlcoholDrinking,
    "Stroke":Stroke,"DiffWalking":DiffWalking,"Diabetic":Diabetic,"PhysicalActivity":PhysicalActivity,"BMI":BMI,
    "Sex":Sex,"Asthma":Asthma,"KidneyDisease":KidneyDisease,"SkinCancer":SkinCancer,"Race":Race,"PhysicalActivity":PhysicalActivity,"SleepTime":SleepTime,
    "PhysicalHealth":PhysicalHealth,"MentalHealth":MentalHealth,"Age":Age,'out':out}


    return render(request,"output.html",context)