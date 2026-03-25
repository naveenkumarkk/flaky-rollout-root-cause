# Fix the broken rollout

A containerized API deployment in `/app` is currently failing.

Your goal is to repair the deployment so that the service is accessible through Nginx on port 8080 and behaves correctly.

Requirements:

1. `curl http://localhost:8080/healthz` must return HTTP 200
2. `curl http://localhost:8080/version` must return valid JSON containing the application version
3. the database migration must be applied before the app begins serving requests
4. the startup flow must be stable when run multiple times

Constraints:

- Work only with the files in `/app`
- Do not rewrite the project from scratch
- Keep changes minimal and production-reasonable
