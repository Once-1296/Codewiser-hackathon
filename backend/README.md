# Cognitive-Aware Study Planner Backend

This repository contains a production-grade FastAPI boilerplate for a
machine learning backend with strict separation of concerns and clean
architecture.

## Project Overview

The backend is designed for a cognitive-aware study planner that will:

- predict user cognitive energy
- classify tasks
- generate an optimized study schedule

The current implementation is intentionally stubbed. It focuses on structure,
interfaces, dependency boundaries, and testability rather than real ML logic.

## Folder Structure

```text
backend/
  app/
    main.py
    api/
    schemas/
    services/
    ml/
    core/
    db/
    utils/
  training/
  tests/
  scripts/
  requirements.txt
  README.md
```

- `app/main.py`: FastAPI application entrypoint.
- `app/api/`: HTTP route definitions and dependency wiring.
- `app/schemas/`: Pydantic request and response models.
- `app/services/`: Business logic layer with no FastAPI dependency.
- `app/ml/`: ML inference and feature engineering stubs.
- `app/core/`: Configuration and shared constants.
- `app/db/`: SQLAlchemy placeholders and CRUD stubs.
- `app/utils/`: Logging and validation helpers.
- `training/`: Stub training and evaluation scripts.
- `tests/`: Pytest-based unit and API tests.
- `scripts/`: Utility scripts for demo data and simulations.

## Run the Server

Install dependencies:

```bash
pip install -r backend/requirements.txt
```

Start the API:

```bash
uvicorn backend.app.main:app --reload
```

## Run Tests

```bash
pytest backend/tests
```

## Notes

- No real ML model is implemented yet.
- All service and ML layers return deterministic placeholder values.
- The codebase is structured to support incremental bottom-up development.
