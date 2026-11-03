# Background Job & Notification Service

A backend project built using **Python, Django, and Django REST Framework** to process email notifications asynchronously using a database-backed job queue.

## About the Project

The Background Job & Notification Service is designed to handle time-consuming tasks such as sending email notifications without making users wait for the entire process to finish.

Instead of sending emails directly during an API request, the system stores jobs in a database and processes them separately through a background worker.

## Technology Stack

- Python
- Django
- Django REST Framework
- SQLite
- Django ORM
- Gmail SMTP
- REST APIs

## Planned Features

- Create background email jobs through REST APIs.
- Store jobs and their details in a database.
- Process jobs asynchronously using a separate worker.
- Send email notifications using Gmail SMTP.
- Implement automatic retry logic for failed jobs.
- Track job execution status.
- Retrieve individual job details through API endpoints.
- Maintain error messages and retry attempts.

## Job Status

- PENDING – Job is waiting for processing.
- PROCESSING – Job is currently being processed.
- COMPLETED – Job has been successfully executed.
- FAILED – Job execution failed after maximum attempts.

## Project Structure

```text
Background-Job-Notification-Service/
│
├── config/
├── jobs/
├── manage.py
├── requirements.txt
└── README.md
```

## Current Development Progress

- [x] Django project setup
- [x] Django REST Framework configuration
- [x] Job model creation
- [x] Job status management
- [ ] Job creation API
- [ ] Background worker implementation
- [ ] Gmail SMTP integration
- [ ] Automatic retry mechanism
- [ ] Job status API
- [ ] API testing

## Learning Objectives

This project focuses on understanding:

- Django REST Framework development
- Background task processing
- Database-backed job queues
- Email integration using SMTP
- Exception handling and retry mechanisms
- REST API design and development

## Author

**Shardendu Prakash Gupta**

Aspiring Python Backend Developer

GitHub: https://github.com/shardendu-gupta

---

*This project is currently under development. More features and improvements will be added as development progresses.*
