#실패했는데 왜 실패한지 다시 찾아보기!!
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

elem = driver.find_elements('<input id="input" type="search" autocomplete="off" spellcheck="false" role="combobox" placeholder="Google 검색 또는 URL 입력" aria-live="polite">')
elem.send.Keys("바다")
elem.send_Keys(Keys.RETURN)