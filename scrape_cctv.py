from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_cctv_video_url():
    # ✅ Chrome 옵션 설정
    options = Options()
    options.add_argument("--headless")  # 화면 없이 실행
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    # ✅ User-Agent 추가 (사이트 차단 우회)
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36")

    # ✅ WebDriver 실행
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    # ✅ CCTV 페이지 로드
    url = "https://www.utic.go.kr/jsp/map/cctvStream.jsp?cctvid=L900033&cctvname=%25EB%258F%2599%25EC%2584%259C%25EC%259A%25B8%25EB%258C%2580%25EC%2582%25AC%25EA%25B1%25B0%25EB%25A6%25AC&kind=EE&cctvip=60204&cctvch=undefined&id=undefined&cctvpasswd=undefined&cctvport=undefined&minX=127.1158589926679&minY=37.44945412462696&maxX=127.13769799468838&maxY=37.46908224990571"
    driver.get(url)

    # ✅ 페이지가 완전히 로드될 때까지 최대 15초 대기
    try:
        video_element = WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.ID, "vid_html5_api"))
        )
        
        # ✅ JavaScript 실행하여 동적으로 생성된 src 추출
        video_src = driver.execute_script("return document.getElementById('vid_html5_api')?.getAttribute('src');")

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
