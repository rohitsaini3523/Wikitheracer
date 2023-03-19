import requests
import  time
import sys
from bs4 import BeautifulSoup
# n = int(input("Enter the Maximum number of pages to visit: "))
dummy_values = ["Search",
                "learn more",
                "Talk",
                "Contributions",
                "Main page",
                "Contents",
                "Current events",
                "Random article",
                "About Wikipedia",
                "Help",
                "Learn to edit",
                "Community portal",
                "Recent changes",
                "Upload file",
                "What links here",
                "Upload file",
                "Special pages",
                "sister projects",
                "Look for pages within Wikipedia that link to this title",
                "try the purge function",
                "case sensitive",
                "redirect",
                "Why was the page I created deleted?",
                "About Wikipedia",
                "Disclaimers", 'Article', 'Read', 'Donate', 'Acèh', 'العربية', 'Արեւմտահայերէն', 'Atikamekw', 'Bamanankan', 'Bosanski', 'Brezhoneg', 'Català', 'Čeština', 'Cymraeg', 'Dagbanli', 'Dansk', 'Deutsch', 'Eesti', 'Ελληνικά', 'Español', 'Esperanto', 'Euskara', 'Eʋegbe', 'فارسی', 'Français', 'Gaeilge', 'Galego', '한국어', 'Hausa', 'Հայերեն', 'Hrvatski', 'Ido', 'Ilokano', 'Ирон', 'Íslenska', 'Italiano', 'Jawa', 'Kapampangan', 'ქართული', 'Ikinyarwanda', 'Kiswahili', 'Коми', 'Kongo', 'Лакку', 'Latina', 'Latviešu', 'Lëtzebuergesch', 'Lietuvių', 'Malagasy', 'مصرى', 'Nederlands', 'Occitan', 'پنجابی', 'Papiamentu', 'Patois', 'Polski', 'Português', 'Română', 'Русский', 'Sängö', 'Sicilianu', 'سنڌي', 'Slovenčina', 'Soomaaliga', 'Sunda', 'Suomi', 'Tagalog', 'Thuɔŋjäŋ', 'Тоҷикӣ', 'Türkçe', 'Удмурт', 'Українська', 'اردو', 'Vahcuengh', 'Võro', '文言', 'Winaray', '吴语', '粵語', '中文']


def getter_links(value):
    got_values = set()
    url = "https://en.wikipedia.org/wiki/" + value
    response = requests.get(url) 
    #check response status
    if response.status_code != 200:
        # print("Error in fetching the page")
        # exit()
        return []
    soup = BeautifulSoup(response.text, "html.parser")
    check = "/wiki"
    for link in soup.find_all("a"):
        link_text = link.text
        link_href = link.get("href")
        if check in str(link_href):
            if link_text not in dummy_values and link_text.isalpha():
                if link_text not in got_values:
                    got_values.add(link_text)
    return got_values

def evaluate(initial, final):
    if (initial == final):
        stored_path = [initial]
        return stored_path
    cnt =0
    visited = set()
    queue = [(initial, [initial])]
    end_link = getter_links(final)
    if(getter_links(initial)==None):
        return None
    if(end_link==None):
        return None
    while queue:
        (page, stored_path) = queue.pop(0)
        if page in visited:
            continue
        visited.add(page)
        cnt+=1
        links = getter_links(page)
        if (len(links) == 0):
            continue
        for link in links:
            if link == final:
                print("Total Visited Pages: ",cnt)
                return str(stored_path + [link])
            queue.append((link, stored_path + [link]))
        cnt+=1
        # if(cnt>n):
        #     print("Total Visited Pages: ",cnt)
        #     print("No Path Found")
        #     break
    return None
#heuristic function to find the path from initial to final word based on distance between two words
def heuristic(initial, final):
    initial = initial.lower()
    final = final.lower()
    distance = 0
    #if final is less than initial then swap the values
    if len(final) < len(initial):
        initial, final = final, initial
    for i in range(len(initial)):
        if initial[i] != final[i]:
            distance += 1
    return distance

#using heuristic function to evaluate the path
def evaluate_using_heuristic(initial, final):
    if(initial==final):
        stored_path = [initial]
        return stored_path
    cnt =0
    #using priority queue to store the path
    queue = [(heuristic(initial, final), initial, [initial])]
    visited = set()
    end_link = getter_links(final)
    if (getter_links(initial) == None):
        return None
    if (end_link == None):
        return None
    while queue:
        (distance, page, stored_path) = queue.pop(0)
        if page in visited:
            continue
        visited.add(page)
        cnt+=1
        links = getter_links(page)
        if(len(links)==0):
            continue
        for link in links:
            if link == final:
                print("Total Visited Pages: ",cnt)
                return str(stored_path + [link])
            queue.append((heuristic(link, final), link, stored_path + [link]))
        cnt+=1
        # if(cnt>n):
        #     print("Total Visited Pages: ",cnt)
        #     print("No Path Found")
        #     break
    return None

def main_function():
    # initial = input("Enter initial Word: ")
    # final = input("Enter final Word: ")
    initial = sys.argv[1]
    final = sys.argv[2]
    start = time.time()
    stored_path = evaluate_using_heuristic(initial, final)
    print("Map to vist form "+initial + " to " + final + " is :" + str(stored_path))
    total = time.time()-start
    print("Exection Time: "+ str(total))
    # got_values contain all possible link
if(__name__ == "__main__"):
    main_function()

#sending input to the function from command line
# python algo.py "Mango" "Seed"