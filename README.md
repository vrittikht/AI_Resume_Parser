AI Resume Parser
AI Resume Parser is an intelligent tool designed to automatically extract structured information from resumes using natural language processing (NLP) techniques. It processes raw resume documents and outputs key candidate details in a format that’s easy to use for analytics, filtering, and integration into downstream applications such as applicant tracking systems (ATS).

Features
1. Resume Text Extraction – Reads resume files and extracts text content.
2. Structured Data Parsing – Identifies standard resume fields such as name, email, phone, skills, education, experience, and more.
3. NLP-powered Understanding – Uses natural language processing to interpret unstructured resume content reliably.
4. Reusable Components – Includes parser logic, utility scripts, and training data to extend or improve performance.
5. Easy Integration – Can be plugged into HR tooling, dashboard UIs, or automated workflows.

Why It Matters
Resume parsing automates what recruiters normally do manually: reading through large volumes of CVs and pulling out essential candidate details. This saves time, reduces human error, and enables fast candidate shortlisting — a core step in modern hiring pipelines. 

Contents
The repository includes:
1. parser.py            # Core resume parsing logic  
2. main.py              # Entry point for running the parser  
3. utils.py             # Helper methods  
4. resume_parser_training.zip  # Training data / models  
5. app.py               # Example runner or UI integration  

Getting Started
1. Clone the repository.
git clone https://github.com/vrittikht/AI_Resume_Parser.git
2.Install dependencies (e.g., Python + NLP libraries like spaCy or NLTK).
3.Run the parser on your set of resumes.
python main.py --input path/to/resume.pdf

Use Cases

1. Recruiters & HR Teams – Automate candidate data extraction at scale.
2. Analytics Teams – Aggregate resume fields into insights (skills trends, experience ranges).
3. Job Platforms – Power structured candidate profiles from uploaded CVs.
