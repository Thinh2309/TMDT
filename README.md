# ***PyWeb - (Python Website Application)***

## *Được chạy bằng Flask với database MySQL*

### How to clone and run code:

1) Open GIT BASH/Terminal
Insert command:

    HTTPS: git clone https://github.com/Thinh2309/Testing.git
    
    SSH: git clone git@github.com:Thinh2309/Testing.git
    
2) Download Python, IDE, MySQL Server and MySQL Workbench.

3) Import database to MySQL Workbench.

4) Open CMD on your computer or Terminal on VSCode.

Insert command:

    cd\your-path
    
Create virtual environment:

    python -m venv venv
    
Activate vir.env:

    venv\Scripts\activate
    
Download required modules:
   
    pip install -r requirements.txt
    
Change env flask run:

    $env:FLASK_APP = "index"
    
Run web:

    flask run

## How to push code to github

1) Batch Execution:
Execute all scripts together in a batch to test the end-to-end functionality:

Install pytest-html (run in terminal after start venv)

 pip install pytest-html
Run tests with HTML report generation

 pytest --html=report.html
Open the HTML report After the tests finish running, a report.html file will be generated.

Open it in any web browser to see a detailed, color-coded report of your test results.
