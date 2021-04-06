from bs4 import BeautifulSoup
import requests
import os
from math import ceil

os.system('clear')

LIMIT = 50
search = input("Indeed! search for? ")
INDEED_URL = f"https://kr.indeed.com/jobs?q={search}&limit={LIMIT}&radius=25"


def get_last_page():
    result = requests.get(INDEED_URL)

    soup = BeautifulSoup(result.text, "html.parser")
    pagination = soup.find("div", {"id": "searchCountPages"}).text.strip()
    page = pagination.split(' ')[-1].replace(',','')
    print(page[:-1])
    # pagination = soup.find("ul", {"class": "pagination-list"})

    # # links = pagination.find_all('a')
    # page = []
    # # 나는 전체 결과 수 에서 50을 나눠 나온 값에 올림한 값이 max!!
    # for link in links:
    #     try:
    #         page.append(int(link.string))
    #     except:
    #         continue

    max_page = ceil(int(page[:-1])/LIMIT)
    return max_page

def extract_job(html):
  title = html.find("h2", {"class": "title"}).find('a')["title"]
  location = html.find("div", {"class":"recJobLoc"})["data-rc-loc"]
  job_id = html.find("h2", {"class": "title"}).find("a")["href"]
  try:
    company = html.find("span", {"class": "company"}).text.strip()
  except:
    company = ''
  if company == "" or location == "":
      company = "누락--------------------------------------"
  return {'title': title, 
          'company': company, 
          'location': location,
          'link': f"https://kr.indeed.com{job_id}"
          }


def extract_indeed_jobs(last_page):

    os.system('clear')
    jobs = []
    for pages in range(last_page):
      print(f"Scrapping INDEED page: {pages}")
      result = requests.get(f"{INDEED_URL}&start={pages*LIMIT}")
      # result = requests.get(f"{INDEED_URL}&start={0}")
      soup = BeautifulSoup(result.text, "html.parser")
      results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
      # print(results)
      for result in results:
        job = extract_job(result)
        jobs.append(job)    
    return jobs

def get_jobs():
  result = get_last_page()
  jobs = extract_indeed_jobs(result)
  return jobs

  os.system('clear')
  # for pages in range(last_page):
  # result = requests.get(f"{INDEED_URL}&start={pages*LIMIT}")
  result = requests.get(f"{INDEED_URL}&start={0}")
  soup = BeautifulSoup(result.text, "html.parser")
  results = soup.find_all("div", {"class": "jobsearch-SerpJobCard"})
  # print(results)  
  for result in results:
    title = result.find("h2", {"class":"title"}).find('a')["title"]
    
    company = result.find("span", {"class":"company"}).text.strip()
    if company == "":
      company = "이름누락-----------------------------------------------------"
    print(f"{title}, {company}") 

    
  return

