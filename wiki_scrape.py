from selenium import webdriver
from bs4 import BeautifulSoup

def get_edits() -> int:

    driver = webdriver.Chrome('C:/Users/Daniil/Downloads/chromedriver_win32/chromedriver')

    #navigates driver to wiki log page with first 1000000000 edits
    driver.get("https://mathwiki.utm.utoronto.ca/wiki/index.php?title=Special:Log&offset=&limit=1000000000&type=&user=")


    #need to login into the wiki to be able to view it so the following code navigates the login
    #page and enters a username and passowrd then clicks login
    
    driver.implicitly_wait(10) #wait 10 seconds when doing a find_element before carrying on

    
    driver.find_element_by_link_text("log in").click()

    username = driver.find_element_by_name("wpName") #finds the username field by its id
    username.clear()
    username.send_keys("insert username") #types in username

    password = driver.find_element_by_id("wpPassword1") #finds password field by its id
    password.clear()
    password.send_keys("password") #types in password

    driver.find_element_by_name("wploginattempt").click() #finds the login button and clicks it

    #the username and passowrd field ids aswell as login button name are found through 
    #going to the page in chrome and pressing F12 and looking through the html to find said ids and name

    html_soup = BeautifulSoup(driver.page_source, "html.parser")

    num_of_wiki_edits = len(html_soup.find('ul').find_all('li'))

    for tag in html_soup.find("ul").find_all("li"):
        print("{0}: {1}".format(tag.name, tag.text))

    #edit = html_soup.li.text
    #print(edit)
    
    
    


    
    driver.quit

    return num_of_wiki_edits
