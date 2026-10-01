# CareLink Security

## 1. Purpose

Security is a core requirement of CareLink because the system handles potentially sensitive healthcare information.

CareLink security is designed around:

- Authentication
- Authorization
- Role-based access control
- Restricted patient-record access
- Secure API access
- Input validation
- Secure database operations
- Protection of credentials and secrets
- Secure deployment configuration

CareLink is a healthcare software engineering project and is not a substitute for a complete clinical compliance or security assessment.

---

## 2. Security Architecture

CareLink uses Django and Django REST Framework (DRF).

```text
Client
  │
  │ HTTPS
  ▼
Django / DRF
  │
  ├── Authentication
  ├── Authorization
  ├── Validation
  ├── Business Rules
  │
  ▼
PostgreSQL
```

The application layer controls access before protected information is returned or modified.

---

## 3. Authentication

CareLink uses an authentication system based on the custom Django `User` model.

Users have roles including:

- Patient
- Healthcare Provider
- Administrator

The backend uses JSON Web Tokens (JWT) through Django REST Framework Simple JWT.

The API should require authentication for protected resources.

### Token configuration

The current configuration uses:

- Short-lived access tokens
- Refresh tokens
- Refresh-token rotation
- Refresh-token blacklisting

The exact token lifetime is controlled by the Django settings.

---

## 4. Authorization

Authentication answers:

> Who is the user?

Authorization answers:

> What is that user allowed to access?

CareLink must enforce both.

Example:

```text
Patient A
  ├── Own profile       ✓
  ├── Own records       ✓
  ├── Own updates       ✓
  └── Patient B data   ✗

Provider A
  ├── Authorized patient data   ✓
  └── Unrelated patient data   ✗
```

Authorization should be enforced at the API/business-logic level rather than relying only on frontend restrictions.

---

## 5. Role-Based Access Control

CareLink uses role-based access control.

### Patient

Patients should be able to:

- View their own profile
- Submit health updates
- Submit recovery updates
- View information they are authorized to access
- Manage permitted appointment and communication functions

### Healthcare Provider

Providers should be able to:

- View authorized patients
- Review authorized patient records
- Review health updates
- Review recovery updates
- Manage permitted provider-side workflows

### Administrator

Administrators may manage system-level functionality according to the application's administrative permissions.

---

## 6. Patient–Provider Authorization

A provider should not automatically gain access to every patient's information.

Access to patient-specific information should be based on an authorized patient-provider relationship.

The `PatientProvider` relationship provides the foundation for this access-control model.

Business rules should verify:

1. The authenticated user has the required role.
2. The target patient exists.
3. The provider is authorized to access the patient.
4. The requested operation is permitted for that role.

---

## 7. Password Security

Passwords must never be stored as plain text.

Django's password hashing mechanisms should be used for:

- Password storage
- Password verification
- Password changes

Application code should never log or expose user passwords.

---

## 8. Secret Management

Sensitive configuration should not be committed to Git.

Examples include:

- Django `SECRET_KEY`
- Database passwords
- Production credentials
- API keys
- External service credentials

Development secrets should be stored in `.env`.

The repository should contain `.env.example` with variable names and safe example values, but not real credentials.

---

## 9. Input Validation

All data received from clients should be validated.

Validation should occur before database operations.

Examples:

- Email validation
- Required-field validation
- Date validation
- Numeric-range validation
- Role validation
- Relationship validation
- Appointment validation

DRF serializers provide a central location for API input validation.

---

## 10. SQL Injection Protection

CareLink uses Django's ORM for database access.

Application code should avoid constructing SQL statements from untrusted user input.

Django ORM queries should be preferred over manually constructed SQL whenever possible.

---

## 11. API Security

Protected API endpoints should require authentication.

The API should:

- Validate JWT authentication
- Enforce permissions
- Validate request data
- Restrict object access
- Return appropriate HTTP status codes
- Avoid exposing sensitive internal information in errors

The frontend should never be treated as the security boundary.

---

## 12. CSRF, CORS and HTTPS

CareLink's backend configuration includes CORS and CSRF origin settings for the frontend.

In production:

- HTTPS should be used.
- Only trusted frontend origins should be allowed.
- Secure cookies should be enabled where applicable.
- Production hosts should be explicitly configured.
- Debug mode should be disabled.

---

## 13. Database Security

PostgreSQL access should use a dedicated database account with only the permissions required by the application.

The database should not be publicly exposed unnecessarily.

Production databases should have:

- Strong credentials
- Restricted network access
- Regular backups
- Appropriate access controls
- Monitoring and recovery procedures

---

## 14. Security Logging

Security-relevant events may include:

- Failed authentication
- Account changes
- Permission failures
- Administrative actions
- Important record access
- Security configuration changes

Logs should avoid storing passwords, tokens, or unnecessary sensitive health information.

---

## 15. Data Minimization

CareLink should only collect information necessary for its defined functionality.

Sensitive information should not be collected simply because it may be useful in the future.

---

## 16. Security Testing

Security testing should cover:

- Unauthorized endpoint access
- Role restrictions
- Patient-provider isolation
- Invalid JWT tokens
- Expired tokens
- Input validation
- SQL injection attempts
- Session/authentication behavior
- CORS configuration
- Production security settings

---

## 17. Security Principles

CareLink follows these principles:

1. Least privilege
2. Defense in depth
3. Secure defaults
4. Explicit authorization
5. Data minimization
6. Secrets outside source control
7. Server-side validation
8. Fail securely
9. Auditability
10. Regular security testing
