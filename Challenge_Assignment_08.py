import requests
from bs4 import BeautifulSoup



BASE_URL = "https://berlinstartupjobs.com"
ENGINEER_URL = f"{BASE_URL}/engineering"
SKILL_URL = f"{BASE_URL}/skill-areas"

skills = ["python", "typescript", "javascript", "rust"]

all_jobs = []


def get_pages_count(url):
    response = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    )
    soup = BeautifulSoup(response.content)
    
    buttons = soup.find("div", class_="bsj-template__b").find("ul", class_="bsj-nav").find_all("a", class_="page-numbers")
    return len(buttons) 

def scrape_page(url):
    response = requests.get(
        url,
        headers={
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
    )
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content)
            
        jobs = soup.find("ul", class_="jobs-list-items").find_all("li", class_="bjs-jlid")
        for job in jobs:
            title = job.find("h4", class_="bjs-jlid__h").text
            url = job.find("a", class_="bjs-jlid__b")["href"]
            company = job.find("a", class_="bjs-jlid__b").text
            description = job.find("div", class_="bjs-jlid__description").text

            job_data = {
                "title" : title,
                "company" : company,
                "description" : description,
                "url" : f"https://weworkremotely.com{url}",
            }
            
            all_jobs.append(job_data)



for page in range(get_pages_count(ENGINEER_URL)):
    url = f"{ENGINEER_URL}/page/{page+1}/"
    print(url)
    scrape_page(url)
print(f"There is(are) {len(all_jobs)} jobs.")    
print(all_jobs)
all_jobs = []

for i in range(len(skills)):
    url = f"{SKILL_URL}/{skills[i]}"    
    print(url)
    scrape_page(url)
    
    print(f"There is(are) {len(all_jobs)} jobs for {skills[i]}")
    print(all_jobs)
    all_jobs=[]