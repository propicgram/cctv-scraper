from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

def get_cctv_video_url():
    # ✅ Selenium 실행 (Chrome headless 모드)
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # 화면 없이 실행
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # 🔥 User-Agent 추가 (사이트가 봇 감지하는 경우 우회)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # ✅ CCTV 페이지 로드
    url = "https://www.utic.go.kr/jsp/map/cctvStream.jsp?cctvid=L900033&cctvname=%25EB%258F%2599%25EC%2584%259C%25EC%259A%25B8%25EB%258C%2580%25EC%2582%25AC%25EA%25B1%25B0%25EB%25A6%25AC&kind=EE&cctvip=60204&cctvch=undefined&id=undefined&cctvpasswd=undefined&cctvport=undefined&minX=127.1158589926679&minY=37.44945412462696&maxX=127.13769799468838&maxY=37.46908224990571"
    driver.get(url)

    # ✅ 페이지가 완전히 로드될 때까지 대기 (기존 5초 → 7초로 증가)
    time.sleep(7)

    # ✅ CCTV 영상 URL 추출
    try:
        video_element = driver.find_element(By.ID, "vid_html5_api")
        video_src = video_element.get_attribute("src")

        if video_src:
            print("✅ CCTV 영상 링크:", video_src)
            return video_src
        else:
            print("🚨 CCTV 영상 링크를 찾을 수 없음")
            return None

    except Exception as e:
        print("❌ 오류 발생:", str(e))
        return None

    finally:
        driver.quit()

# ✅ 실행
if __name__ == "__main__":
    get_cctv_video_url()
