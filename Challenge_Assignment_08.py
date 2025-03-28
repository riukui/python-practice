import requests
from bs4 import BeautifulSoup


class Job:
    # Job information Class
    def __init__(self, title, company, description, links):
        self.title = title
        self.company = company
        self.description = description
        self.links = links

    def __repr__(self):
        return f"Job(title='{self.title}', company='{self.company}')"


class JobScraper:
    # URL
    MAIN_URL = "https://berlinstartupjobs.com/"
    ENGINEERING_URL = f"{MAIN_URL}engineering/"
    # skill_Array
    SKILL_AREAS = [
        f"{MAIN_URL}skill-areas/python",
        f"{MAIN_URL}skill-areas/typescript",
        f"{MAIN_URL}skill-areas/javascript",
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
        return BeautifulSoup(response.text, "html.parser")

    def get_total_pages(self, ENGINEERING_URL):
        # ENGINEERING_URL에서 총 페이지 수 가져오기
        soup = self.fetch_html(ENGINEERING_URL)
        page_buttons = soup.find_all("a", class_="page-numbers")

        if not page_buttons:
            return 1
        total_pages = max(
            int(btn.text) for btn in page_buttons if btn.text.isdigit())
        return total_pages

    def scrape_jobs(self, url):
        # 현재 URL에서 직무 정보 스크래핑
        soup = self.fetch_html(url)
        jobs = soup.find_all("div", class_="bjs-jlid__wrapper")

        for job in jobs:
            # 회사 이름
            company = job.find("a", class_="bjs-jlid__b")
            # 직무 제목
            title = job.find("h4", class_="bjs-jlid__h").find("a")
            # 설명
            description = job.find("div", class_="bjs-jlid__description")
            # 직무 링크
            links = job.find_all("a", class_="bjs-bl bjs-bl-whisper")
            # 직무명, 직무 링크를 넣을 딕션
            link_dict = {}
            for link in links:
                link_text = link.text
                link_href = link["href"]
                link_dict[link.text] = link["href"]
            self.jobs.append(Job(title, company, description, link_dict))

    def scrape_all(self):
        # 모든 URL에서 직무 정보 스크래핑
        # 공통 엔지니어링 페이지 스크래핑
        total_pages = self.get_total_pages(self.ENGINEERING_URL)
        print(f"(Engineering)에서 총 {total_pages} 페이지 발견")

        for page in range(1, total_pages + 1):
            page_url = f"{self.ENGINEERING_URL}/page/{page}/" if page > 1 else self.ENGINEERING_URL
            print(f"📌 Scraping: {page_url}")
            self.scrape_jobs(page_url)

        # 특정 스킬 페이지 스크래핑
        for SKILL_AREA in self.SKILL_AREAS:
            self.scrape_jobs(SKILL_AREA)

        self.display_jobs()

    def display_jobs(self):
        # 직무 정보 출력
        for job in self.jobs:
            print(f"Company: {job.company.text}")
            print(f"Title: {job.title.text}")
            print(f"Description: {job.description.text}")
            print("Links:\n")
            for text, url in job.links.items():
                print(f"{text}: {url}")
            print("\n----------------------------------------\n")

    def get_pages(self, url):
        # 페이지 수 수집
        soup = self.fetch_html(url)
        buttons = len(soup.find_all("a", class_="page-numbers"))
        for i in range(buttons):
            self.scrape_jobs(f"{self.ENGINEERING_URL}/page/{i+1}")
        total_pages = get_pages(self.ENGINEERING_URL)
        return len(soup.find_all("a", class_="page-numbers"))


# 실행 코드
if __name__ == "__main__":
    scraper = JobScraper()
    scraper.scrape_all()
    scraper.display_jobs()