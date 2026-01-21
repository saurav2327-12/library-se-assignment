# User Stories – Library Book Management System

This document lists the user stories implemented in the Library Book Management System.
The user stories are organized sprint-wise, following Agile development practices.

---

## Sprint 1: Book Registration

### US-1: Add a New Book
**As a** librarian  
**I want to** add a new book with Book ID, Title, and Author  
**So that** the book can be stored in the library system  

**Acceptance Criteria:**
- Book ID must be unique
- Book details are stored in memory
- Book status is set to "Available" by default

---

### US-2: Prevent Duplicate Book IDs
**As a** librarian  
**I want to** prevent adding books with duplicate Book IDs  
**So that** data consistency is maintained  

**Acceptance Criteria:**
- Adding a book with an existing Book ID raises an error
- Duplicate entries are not stored

---

## Sprint 2: Borrow and Return Book

### US-3: Borrow an Available Book
**As a** library user  
**I want to** borrow a book that is available  
**So that** I can read the book  

**Acceptance Criteria:**
- Book status changes from "Available" to "Borrowed"
- Borrowing succeeds only if the book is available

---

### US-4: Prevent Borrowing an Already Borrowed Book
**As a** library user  
**I want to** be prevented from borrowing a book that is already borrowed  
**So that** the same book is not issued to multiple users  

**Acceptance Criteria:**
- Borrowing an already borrowed book raises an error
- Book status remains unchanged

---

### US-5: Return a Borrowed Book
**As a** library user  
**I want to** return a borrowed book  
**So that** it becomes available for others  

**Acceptance Criteria:**
- Book status changes from "Borrowed" to "Available"
- Returned book can be borrowed again

---

## Sprint 3: Library Report

### US-6: Generate Library Status Report
**As a** librarian  
**I want to** generate a report of all books  
**So that** I can view the current status of the library  

**Acceptance Criteria:**
- Report contains Book ID, Title, Author, and Status
- Report includes all books in the system
- Status is shown as "Available" or "Borrowed"

---

## Notes
- All user stories are implemented using in-memory data structures.
- Each user story is linked to unit tests and corresponding Git sprint tags.
