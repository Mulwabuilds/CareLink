# CareLink API Documentation

## 1. Overview

CareLink exposes a REST API through Django REST Framework (DRF).

The API provides the backend interface used by the frontend and other authorized clients.

Base API structure:

```text
/api/
```

Current application namespaces include:

```text
/api/auth/
/api/accounts/
/api/providers/
/api/records/
/api/appointments/
/api/messaging/
/api/notifications/
/api/administration/
```

The patients namespace will be included once the dedicated patients application is implemented:

```text
/api/patients/
```

---

# 2. Authentication

CareLink uses JWT authentication.

The authentication flow is conceptually:

```text
Client
  │
  │ credentials
  ▼
Login Endpoint
  │
  ▼
Access + Refresh Tokens
  │
  ▼
Authenticated API Requests
```

Protected requests should include the access token using:

```text
Authorization: Bearer <access_token>
```

---

# 3. Token Endpoints

## Refresh Access Token

```http
POST /api/auth/refresh/
```

Purpose:

- Obtain a new access token using a valid refresh token.

The endpoint is provided by Simple JWT.

---

# 4. Accounts API

Base path:

```text
/api/accounts/
```

The accounts application is responsible for user identity and authentication-related functionality.

Expected responsibilities include:

- Registration
- User information
- Authentication-related operations

Exact endpoint behavior should follow the implemented Django URL configuration.

---

# 5. Providers API

Base path:

```text
/api/providers/
```

Provider functionality includes:

- Provider profiles
- Provider information
- Patient-provider relationships
- Provider-side patient management

Provider access must be restricted to authorized operations.

---

# 6. Patients API

Base path:

```text
/api/patients/
```

The patients application is intended to contain patient-specific domain functionality.

Potential resources include:

- Patient profile
- Contact information
- Emergency contact information

This namespace should only be considered active after the patients application and URLs are implemented.

---

# 7. Records API

Base path:

```text
/api/records/
```

The records application manages:

- Medical records
- Health updates
- Recovery updates

Conceptually:

```text
/api/records/
       │
       ├── medical records
       ├── health updates
       └── recovery updates
```

Patient-specific resources must enforce authorization.

---

# 8. Appointments API

Base path:

```text
/api/appointments/
```

Appointment records contain:

- Patient
- Provider
- Scheduled date/time
- Reason
- Status
- Creation timestamp

Current status values:

```text
PENDING
CONFIRMED
COMPLETED
CANCELLED
```

---

# 9. Messaging API

Base path:

```text
/api/messaging/
```

The messaging system manages messages between users.

A message contains:

```text
sender
recipient
content
sent_at
read_at
```

Messaging endpoints must ensure users cannot access conversations they are not authorized to access.

---

# 10. Notifications API

Base path:

```text
/api/notifications/
```

Notifications belong to individual users.

Current notification types include:

```text
APPOINTMENT
MESSAGE
HEALTH
SYSTEM
```

Users should only receive and access their own notifications.

---

# 11. Administration API

Base path:

```text
/api/administration/
```

This namespace provides administrative functionality.

The initial implementation is intentionally limited and can be expanded as administrative requirements become clearer.

Administrative endpoints must be restricted to authorized administrative users.

---

# 12. HTTP Methods

The API uses standard REST-style HTTP methods.

| Method | Purpose |
|---|---|
| GET | Retrieve resources |
| POST | Create resources |
| PUT | Replace/update a resource |
| PATCH | Partially update a resource |
| DELETE | Delete a resource |

Not every endpoint needs to support every method.

---

# 13. Common HTTP Status Codes

| Status | Meaning |
|---|---|
| 200 | Request successful |
| 201 | Resource created |
| 204 | Successful request with no response body |
| 400 | Invalid request |
| 401 | Authentication required or invalid |
| 403 | Authenticated but not authorized |
| 404 | Resource not found |
| 409 | Conflict |
| 500 | Unexpected server error |

---

# 14. Request Validation

Client input should be validated through DRF serializers.

Validation should cover:

- Required fields
- Data types
- Field lengths
- Valid choices
- Relationships
- Business rules
- Authorization requirements

The API should return structured validation errors rather than allowing invalid data to reach the database.

---

# 15. Pagination

The CareLink DRF configuration uses pagination for API result sets.

The current default page size is:

```text
20
```

Pagination helps prevent large responses from unnecessarily consuming server and client resources.

---

# 16. Authorization Model

API authorization follows the CareLink role model:

```text
                  Authenticated User
                         │
             ┌───────────┼───────────┐
             ▼           ▼           ▼
          Patient     Provider      Admin
             │           │           │
             ▼           ▼           ▼
        Own data     Authorized    System
                     patients     functions
```

Role checks alone are not sufficient for patient-specific resources.

The API should also verify the relevant patient-provider relationship.

---

# 17. API Security Rules

The API should:

- Require authentication for protected endpoints.
- Validate JWTs.
- Enforce permissions.
- Validate request data.
- Filter querysets by authorization.
- Avoid exposing internal exceptions.
- Avoid returning unnecessary sensitive information.
- Use HTTPS in production.

---

# 18. Example Authenticated Request

Conceptually:

```http
GET /api/records/
Authorization: Bearer <access_token>
```

The server should authenticate the token and then apply the appropriate authorization rules before returning records.

---

# 19. API Development Principle

The API should remain consistent with the Django domain model.

```text
Frontend
   │
   ▼
REST API
   │
   ▼
Django Applications
   │
   ▼
PostgreSQL
```

API documentation should be updated whenever endpoints, serializers, permissions, or data models change.
