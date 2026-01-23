Software Engineering Assignment #1
Agile Development with Git and Unit Testing

CS2042
09-01-2026

Assignment Objective

Implement a small software system by following a three-sprint Agile (sprint-based) de-
velopment process using Git for version control and unit testing for verification. De-
velop a Library Book Management System using in-memory data structures only (no

database).
1 Technology Constraints
• Programming Language: Python
• Testing Framework: unittest
• Version Control System: Git
• Database usage is not allowed
2 Agile + Git Rules (Must Follow)
• The assignment must be completed in three sprints (Sprint-1, Sprint-2, Sprint-3).
• No direct commits to main are permitted.
• Each sprint must:
– be developed in its own branch: feature/sprint-X
– include unit tests for that sprint
– be merged into main only after all tests pass
– be tagged on main after merge: v0.1, v0.2, v0.3
– update docs/TRACEABILITY.md
3 Sprint Requirements
3.1 Sprint 1: Book Registration
Sprint Goal: Add and store book details.
• Add a book with Book ID, Title, Author
• Duplicate Book IDs must be rejected

1

Minimum Unit Tests (Sprint-1):
• Successful book addition
• Duplicate book addition raises an error
Git Requirements (Sprint-1):
• Branch: feature/sprint-1
• Tag after merge: v0.1
3.2 Sprint 2: Borrow and Return Book
Sprint Goal: Manage borrowing status.
• Borrow a book
• Return a book
• Borrowing an already borrowed book must raise an error
Minimum Unit Tests (Sprint-2):
• Borrowing an available book
• Borrowing an unavailable book raises an error
• Returning a book updates status correctly
Git Requirements (Sprint-2):
• Branch: feature/sprint-2
• Tag after merge: v0.2
3.3 Sprint 3: Library Report
Sprint Goal: Generate a library status report.
• Generate a report containing:
– Book ID
– Title
– Author
– Status (Available / Borrowed)
Minimum Unit Tests (Sprint-3):
• Report contains header
• Report contains at least one book entry
Git Requirements (Sprint-3):
• Branch: feature/sprint-3
• Tag after merge: v0.3

2

4 Suggested Project Structure
library - se /
| - - src /
| -- library . py
| - - tests /
| -- test_library . py
| - - docs /
| -- TRACEABILITY . md
| -- USER_STORIES . md
README . md
. gitignore

5 What You Must Submit
Submit a pdf report with the github repo link. The pdf should be named as
rollnumber_swe - task1 . pdf
Example : 230101090 _swe - task1 . pdf
1) GitHub Repository Link
The repository must contain:
• Source code (src/) and unit tests (tests/)
• docs/USER STORIES.md
• docs/TRACEABILITY.md
• Git tags on main: v0.1, v0.2, v0.3
2) Submission Report PDF (3–4 pages)
Submit a separate PDF report (3–4 pages) explaining your work. The report must follow the
format given below.
6 Submission Report PDF Format (3–4 Pages)
Create a PDF report with these sections (use headings exactly):
Title Page (Half page)
Include:
• Assignment title
• Course code
• Student name and roll number
• Date of submission
• GitHub repository link

3

1. Problem Statement (3–5 lines)
Explain what system you built and what it is supposed to do.
2. Agile Plan (Sprint-wise) (Half page)
Write a short plan:
• Sprint-1 goal + key features delivered
• Sprint-2 goal + key features delivered
• Sprint-3 goal + key features delivered
3. Implementation Summary (Sprint-wise) (1 page)
For each sprint (Sprint-1 to Sprint-3), write:
• Features implemented (bullet points)
• Main functions/classes added (e.g., add book(), borrow book(), etc.)
• Major design choice (e.g., data structure used: dictionary)
4. Testing Summary (Half page)
Mention:
• Total number of test cases written per sprint
• What each set of tests verifies (in 2–3 bullets)
• Command used to run tests:
python -m unittest discover -s tests -p " test_ *. py " -v

5. Traceability (Mandatory) (Half page)
Include:
• A brief explanation (2–3 lines): traceability links user stories to code, tests, and releases.
• Paste your final traceability table from docs/TRACEABILITY.md.
6. Git Evidence (Mandatory) (Half to 1 page)
Copy-paste the outputs of the following commands into the report:
git log -- all -- oneline -- decorate -- graph
git branch -a
git tag
Also include a 2–3 line explanation showing:
• Sprint branches were used
• Merges happened into main
• Tags exist for all 3 sprints

4

7. Conclusion (3–6 lines)
Summarize what you learned about:
• sprint discipline
• git discipline (branches/merge/tag)
• testing / TDD mindset
• traceability
Important Notes
• Assessment is primarily for software engineering process adherence, not just working
code.
• If your repository does not contain tags v0.1, v0.2, v0.3, it will be considered incomplete.
• If TRACEABILITY.md is missing or not updated sprint-wise, it will be considered incomplete.
