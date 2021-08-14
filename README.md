# CLI tool to scrap links from websites.  

### Run with Docker:
Build project with:
```bash
docker build -t extractor .
```
Run with:
```bash
docker run --rm extractor <args>
```
Example: Extract domains found from hrefs on github.com  
```bash
docker run --rm extractor --url https://www.github.com -d
```
### Run with Python:
Install dependencies with:
```bash
pip3 install -r requirements.txt
```
Run with:
```bash
python3 src/main.py
```
View available options with:
```bash
python3 src/main.py -h
```
Example: Extract links, scripts and assets from google.com
```bash
python3 src/main.py --url https://www.google.com -a
```