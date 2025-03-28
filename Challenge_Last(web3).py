import requests
from bs4 import BeautifulSoup
import time


class Job:
    # Job information Class
    def __init__(self, title, company, links):
        self.title = title
        self.company = company
        self.links = links

    def __repr__(self):
        return f"Job(title='{self.title}', company='{self.company}')"


class JobScraper:
    # URL
    MAIN_URL = "https://web3.career/"
    # skill_Array
    SKILL_AREAS = [
        f"{MAIN_URL}python-jobs",
        f"{MAIN_URL}javascript-jobs",
        f"{MAIN_URL}java-jobs",
    ]

    def __init__(self):
        self.jobs = []

    def fetch_html(self, url):
        # 주어진 URL에서 HTML을 가져옴
        headers = {
            "User-Agent":
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
            "AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }
        response = requests.get(url, headers=headers)
        # 
        if response.status_code != 200:
            print(f"❌ 요청 실패: {response.status_code}")
            return None
        return BeautifulSoup(response.text, "html.parser")

    def scrape_jobs(self, url):
        # 현재 URL에서 직무 정보 스크래핑
        soup = self.fetch_html(url)
        jobs = soup.find_all("div", class_="col")

        for job in jobs:
            # print(job.prettify())
            # 회사 이름
            company = job.find("h3", class_="")
            # 직무 제목
            title = job.find("h2", class_="fs-6 fs-md-5 fw-bold my-primary")
            # 설명 
            # description = job.find("div", class_="text-dark-grey-text px-3 pt-2").find("p")
            # 직무 링크
            links = job.find_all("a", class_="text-shadow-1px")
            # 직무명, 직무 링크를 넣을 딕션
            link_dict = {}
            for link in links:
                link_text = link.text
                link_href = link["href"]
                link_dict[link.text] = link["href"]
            self.jobs.append(Job(title, company, link_dict))
            time.sleep(1)

    def scrape_all(self):
        # 특정 스킬 페이지 스크래핑
        for SKILL_AREA in self.SKILL_AREAS:
            self.scrape_jobs(SKILL_AREA)

        self.display_jobs()

    def display_jobs(self):
        # 직무 정보 출력
        for job in self.jobs:
            print(f"Company: {job.company}")
            print(f"Title: {job.title}")
            print("Links:\n")
            for text, url in job.links.items():
                print(f"{text}: {url}")
            print("\n----------------------------------------\n")

# 실행 코드
if __name__ == "__main__":
    scraper = JobScraper()
    scraper.scrape_all()
    scraper.display_jobs()