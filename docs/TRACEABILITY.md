| Sprint | User Story | Code | Test | Tag |
|------|-----------|------|------|-----|
| 1 | Add books | add_book() | test_add_book_success | v0.1 |
## Sprint-2: Borrow and Return Book

| Requirement | Code Function | Test Case |
|------------|--------------|-----------|
| Borrow book | borrow_book() | test_borrow_available_book |
| Prevent double borrow | borrow_book() | test_borrow_unavailable_book_raises_error |
| Return book | return_book() | test_return_book_updates_status |
## Sprint-3: Library Report

| Requirement | Code Function | Test Case |
|------------|--------------|-----------|
| Generate report header | generate_report() | test_report_contains_header |
| Report contains book entry | generate_report() | test_report_contains_book_entry |
