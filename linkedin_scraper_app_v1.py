from flask import Flask, request, jsonify
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import json
import os

app = Flask(__name__)

def setup_proxy_driver():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=chrome_options)
    return driver

@app.route('/scrape_linkedin', methods=['GET'])
def scrape_linkedin():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL is required"}), 400

    driver = setup_proxy_driver()
    temp_html = url.split('/')[-2]
    profile_data = {}

    try:
        driver.get(url)
        page_source = driver.page_source

        script_element = driver.find_element(By.CSS_SELECTOR, 'script[type="application/ld+json"]')
        json_data = script_element.get_attribute('innerHTML')

        profile_data = json.loads(json_data)

        if not os.path.exists('output'):
            os.makedirs('output')

        with open(f'output/{temp_html}.json', 'w', encoding='utf-8') as f:
            json.dump(profile_data, f, ensure_ascii=False, indent=4)

    except Exception as e:
        return jsonify({"error": f"An error occurred while scraping: {str(e)}"}), 500
    finally:
        driver.quit()

    return jsonify(profile_data)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
