import os
from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd
import time

df = pd.read_csv('C:/Users/Sangb/Desktop/PJ3/responsive_travel_website/assets/model_edit.csv')

app = Flask(__name__)

# 크롤링 라이브러리 import
import requests
from bs4 import BeautifulSoup

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/recommend', methods=['GET','POST'])
def home():
    data1 = request.form['테마']
    
    pl_list = df.sort_values(f'{data1}',ascending = False).head(10)
   
        
    return render_template('after.html', data=pl_list)

@app.route('/recommend/info', methods=['POST'])
def info():
    data2 = request.form["chk_info"]

    req = requests.get(f'https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query={data2}')
    
    # 이런 식으로 HTML에 있는 코드를 다 가져온다
    soup = BeautifulSoup(req.text, 'html.parser')

    try:
        title = soup.find('span', class_='_3XamX')    
        title = title.text
    except:
        try:
            title = soup.find('span', class_='_3Apve')
            title = title.text
        except:
            title = '정보없음'  
   
    try:   
        number = soup.find('span', class_='_3ZA0S')
        number = number.text
    except:
        try:
            number = soup.find('div', class_='OE7yL')
            number = number.text
        except:
            number = '-'

    try:
        address = soup.find('span', class_ = '_2yqUQ')
        address = address.text
    except:
        try:
            address = soup.find('span', class_='_2Po-x')
            address = address.text
        except:
            address = '-'

    try:
        story = soup.find('span', class_ = 'WoYOw')
        story = story.text
    except:
        story = '-'


    return render_template('info.html', d1 = title, d2= number, d3= address, d4 = story)
    
 





if __name__ == "__main__":
    app.run(debug=True)