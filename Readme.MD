TREE: OR THE DIRECTORY YOU GUYS NEED TO PUT EVERYTHING IN

PROJECT_ROOT/
│
├── browser/
│   ├── templates/
│   │   ├── index.html
│   │   └── search_results.html
│   │
├── app.py
├── crawler.py
└── urls.json 

To set up the project directory, create a structure with a folder named browser, which contains another folder called templates holding the files index.html and search_results.html. 
Additionally, place the files app.py, crawler.py, and urls.json directly in the project root. Ensure that Python is installed on your system; you can verify this by running python --version in your terminal. 
To generate the urls.json file, execute python crawler.py in the terminal, and if the generated file has a different name, rename it to urls.json. 
It is crucial to confirm that the urls.json file is populated with the necessary links before proceeding to run the application. This can be done by executing python app.py in your terminal. 
After running the application, navigate to the displayed localhost URL (usually http://127.0.0.1:5000/) in your web browser. If any errors occur, check the terminal output for guidance or refer to the project documentation for troubleshooting steps.

