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

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # ✅ CCTV 페이지 로드
    url = "https://www.utic.go.kr/jsp/map/cctvStream.jsp?cctvid=L900033"
    driver.get(url)

    # ✅ 페이지가 완전히 로드될 때까지 대기
    time.sleep(5)

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
