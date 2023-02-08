The Following program is built on python 3.11.1

The Following libraries were used:

* bs4
  * BeautifulSoup
* requests
* time

## Testing

Built and tested on Windows 11 Insider Preview (10.0.25290.1010) and Python 3.11.1 using pip for package management. Dependencies are listed in requirements.txt

---

Step 1: Clone the Repository

```
git clone https://github.com/rohitsaini3523/wikitheracer
```

Step 2:  Open the wikitheracer directory and create a virtual environement

```
python -m venv venv
```

Step3: activate Virtual Environment

```
venv\Scripts\activate
```

Step4: install required packages

```
pip install -r requirements.txt
```

Step5: Run algo.py

```
python algo.py
```

Example:

Enter the Maximum number of pages to visit: 10
Enter initial Word: Mango
Enter final Word: Apple
Total Visited Pages:  1
Map to vist form Mango to Apple is :['Mango', 'Apple']
Exection Time: 0.4536592960357666

The program will ask you to enter number of link it parse to find the final state if it found will print the total visited page other wise it will print NONE and Show "NO path found"

---

* [X] Milestone 1: BFS(Simple Breadth First Search)
