import undetected_chromedriver as uc
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

commentsDict = ['good','amazing one','keep going','excellent','next video please','sub to your channel','shared to others','made my day','keep it up','sensational','rock it','challenge it','post video daily','work was amazing','needed more edit','edit was awesome',
'what a video man','watched yesterday','your are genious','faster than light','your work needed success','new fan of you','keep rock dude','copy cat','link the video','listening','writing','reading','playing',] #replace with your words

email = 'when123@gmail.com\n'      #replace with your gmail         
password = 'pass123$%\n'           #replace with your password     

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver,20)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
#time.sleep(2)
wait.until(EC.visibility_of_element_located((By.NAME,'Passwd'))).send_keys(password)
time.sleep(2)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  

time.sleep(7)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[2]/div[2]/ytd-reel-video-renderer[1]/div[1]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon').click() #automatically pause the youtube shorts

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[2]/div[2]/ytd-reel-video-renderer[1]/div[2]/ytd-reel-player-overlay-renderer/div[2]/div[4]/ytd-button-renderer/yt-button-shape/label').click() #click the comment box element

time.sleep(2)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(3)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(3)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(3)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(3)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

driver.close()

email = 'virat@1273@gmail.com\n'   #replace with your mail         
password = 'pass1243$%\n'           #replace with your password     

driver = uc.Chrome(use_subprocess=True)
wait = WebDriverWait(driver,5)
url = 'https://accounts.google.com/AddSession?continue=https%3A%2F%2Fwww.youtube.com%2Fsignin%3Faction_handle_signin%3Dtrue%26app%3Ddesktop%26hl%3Den-GB%26next%3D%252F&hl=en-GB&passive=false&service=youtube&uilel=0'
driver.get(url)

wait.until(EC.visibility_of_element_located((By.NAME,'identifier'))).send_keys(email)
#time.sleep(2)
wait.until(EC.visibility_of_element_located((By.NAME,'Passwd'))).send_keys(password)
time.sleep(2)

with open("urls.txt") as f:
    for url in f:
        driver.get(url)  
        
time.sleep(7)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[2]/div[2]/ytd-reel-video-renderer[1]/div[1]/div/ytd-shorts-player-controls/yt-icon-button[1]/button/yt-icon').click() #automatically pause the youtube shorts

time.sleep(3)

driver.find_element_by_xpath('/html/body/ytd-app/div[1]/ytd-page-manager/ytd-shorts/div[2]/div[2]/ytd-reel-video-renderer[1]/div[2]/ytd-reel-player-overlay-renderer/div[2]/div[4]/ytd-button-renderer/yt-button-shape/label').click() #click the comment box element

time.sleep(2)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(3)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(3)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(3)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(3)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(5)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

time.sleep(3)

WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "ytd-comments ytd-comment-simplebox-renderer")))

driver.find_element_by_css_selector("ytd-comments ytd-comment-simplebox-renderer div#placeholder-area").click()

driver.find_element_by_css_selector("#contenteditable-root").send_keys(random.choice(commentsDict))

time.sleep(2)

send_comment_button = driver.find_element_by_id("submit-button").click()

driver.close()
