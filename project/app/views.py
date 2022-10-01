
from django.shortcuts import  render, redirect
import requests
from bs4 import BeautifulSoup
from requests.compat import quote_plus
import json
import pandas as pd
import numpy as np
from sklearn import decomposition
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
import matplotlib.pyplot as plt
from sklearn.preprocessing import Normalizer
from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn import preprocessing 
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from django.http import request
from django.shortcuts import redirect, render
from django.views import View
from .models import Student
from .forms import StudentRegistrationForm , Test
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from app.dicto import ro
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB


def index(request):
		return render(request, 'index.html', {})     

def profile(request):
		username = request.user
		return render(request, 'profile.html', {'username':username})  

def test(request):
	form = Test()
	x={}
	if request.method == 'POST':
		form = Test(request.POST)
		x['academic_percentage_in_operating_system']= request.POST.get('academic_percentage_in_operating_system')
		x['percentage_in_algorithm']=request.POST.get('percentage_in_algorithm')		
		x['percentage_in_programming_concepts']=request.POST.get('percentage_in_programming_concepts')		
		x['percentage_in_software_engineering']=request.POST.get('percentage_in_software_engineering')		
		x['percentage_in_computer_networks']=request.POST.get('percentage_in_computer_networks')		
		x['percentage_in_electronics_subjects']=request.POST.get('percentage_in_electronics_subjects')		
		x['percentage_in_computer_architecture']=request.POST.get('percentage_in_computer_architecture')		
		x['percentage_in_mathematics']=request.POST.get('percentage_in_mathematics')		
		x['percentage_in_communication_skills']=request.POST.get('percentage_in_communication_skills')		
		x['how_many_hours_in_a_day_you_can_work']=request.POST.get('how_many_hours_in_a_day_you_can_work')		
		x['Rate_your_logical_quotient']=request.POST.get('Rate_your_logical_quotient')		
		x['How_may_hackathon_have_you_participated']=request.POST.get('How_may_hackathon_have_you_participated')		
		x['Rate_your_coding_skills']=request.POST.get('Rate_your_coding_skills')		
		x['Rate_your_public_speaking']=request.POST.get('Rate_your_public_speaking')		
		x['can_work_long_time_before_system']=request.POST.get('can_work_long_time_before_system')
		x['self_learning_capability']=request.POST.get('self_learning_capability')
		x['which_certifications_do_you_prefer']=request.POST.get('which_certifications_do_you_prefer')
		x['any_talenttests_taken']=request.POST.get('any_talenttests_taken')
		x['scale_your_reading_and_writing_skills']= request.POST.get('scale_your_reading_and_writing_skills')
		x['scale_your_memory_capability_score'] = request.POST.get('scale_your_memory_capability_score')
		x['Interested_subjects'] = request.POST.get('Interested_subjects')
		x['interested_career_area'] = request.POST.get('interested_career_area')
		x['what_do_you_prefer_job_or_higher_studies'] = request.POST.get('what_do_you_prefer_job_or_higher_studies')
		x['type_of_company_you_prefer'] = request.POST.get('type_of_company_you_prefer')
		x['intereaction_with_seniors'] = request.POST.get('intereaction_with_seniors')
		x['do_you_love_games'] = request.POST.get('do_you_love_games')
		x['type_of_books_you_prefer'] = request.POST.get('type_of_books_you_prefer')
		x['most_likely_behaviour'] = request.POST.get('most_likely_behaviour')
		x['what_you_prefer_managemet_or_technical'] = request.POST.get('what_you_prefer_managemet_or_technical')
		
		x['have_you_ever_worked_with_teams'] = request.POST.get('have_you_ever_worked_with_teams')
		x['Are_you_an_Introvert']= request.POST.get('Are_you_an_Introvert') 
		
		print(x)
		career = fun(x)
		context= {'career':career}
		return render(request,'generated_career.html',context)
	context = {'form':form}
	return render(request,'test.html',context)

def fun(dict1):
	return "Complete Function fun(dict1) in views.py in app folder to predict the proper career from roo_data.csv "

def login(request):
 return render(request, 'login.html')

class CustomerRegistrationView(View):
	def get(self,request):
		print("get")
		form = StudentRegistrationForm()
		context = {'form':form}
		return render(request,'register.html',context)
	def post(self,request):
		print("post")
		form = StudentRegistrationForm(request.POST)
		if form.is_valid():
			messages.success(request,"Congratulations!! Register Successfully")
			form.save()
			print("post")
		context = {'form':form}
		return render(request,'register.html',context)

def roadmap(request,career):
	
	ans = "Also find generate the roadmap for predictaed career "
	return render(request,'roadmap.html',{'ans':ans})
		

BASE_URL = 'https://udemy.com/courses/search/?q={}'
def courses(request,career):
	
	final_url = BASE_URL.format(quote_plus(career))
	response = requests.get(final_url)
	data = response.text
	soup = BeautifulSoup(data , features='html.parser')
	print(final_url)
	main = soup.find('div',{'class':'main-content'})
	print("MAIN--------------------------")
	print(main)
	DIV1= soup.find('div',{'class':'ud-app-loader ud-component--search--search ud-app-loaded'})
	print("DIV-----------------------------")
	print(DIV1)
	course_listing = soup.findAll('div',{'class':'course-card--main-content--2XqiY'})
	# class="udlite-heading-md course-card--course-title--vVEjC"
	# course-card--main-content--2XqiY course-card--has-price-text--1c0ze
	context = {}
	print(course_listing)
	for course in course_listing:
		link = course.find('a').get('href')
		heading = course.find('a').text
		context[heading]=link
	print(context)
	return render(request,'courses.html')



def about(request):
	return render(request,'about.html')
	