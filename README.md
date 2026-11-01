# Python Development – End-to-End Data Pipeline

A production-style data engineering project, built step by step to practise
real-world workflows: Python ingestion, Databricks lakehouse, dbt
transformations, Airflow orchestration, testing, and CI/CD.


## Architecture (planned)

```
[Data source API] → Python extractor → Databricks (Delta Lake)
                                         ├── bronze: raw data as ingested
                                         ├── silver: cleaned, deduplicated (dbt staging)
                                         └── gold:   business-ready tables (dbt marts)
                                                     ↓
                                               [dashboard / output]
```

- **Orchestration:** Airflow (with retries and failure alerts)
- **Data quality:** dbt tests at each layer

## Data source
Data: Energy-Charts.info, licensed under CC BY 4.0

## Tech stack
- Python 3.12, managed with [uv](https://docs.astral.sh/uv/)
- Databricks (Free Edition) with Delta Lake, medallion architecture (bronze / silver / gold)
- dbt with the `dbt-databricks` adapter for transformations and data tests
- Airflow for orchestration
- pytest for unit tests
- Docker / docker-compose for local setup
- GitHub Actions for CI/CD

## Project structure

```
src/python_development/   # Python source code (ingestion, utilities)
tests/                    # pytest unit tests
transform/                # dbt project (coming soon)
dags/                     # Airflow DAGs (coming soon)
```

## Getting started

```bash
git clone https://github.com/taybkho/python-development.git
cd python-development
uv sync
cp .env.example .env      # then fill in your values
uv run pytest
```

## Development workflow
- Every change starts as a GitHub issue
- Work happens on a feature branch (`feat/...`, `fix/...`, `chore/...`)
- Changes go through a pull request with review before merging into `main`
- `main` is protected: no direct pushes

## Roadmap
- [x] Project setup (uv, repo structure, branch protection)
- [x] API extractor + unit tests
- [ ] Load raw data into Databricks (bronze layer)
- [ ] dbt silver and gold models + data tests
- [ ] Airflow DAG orchestrating ingestion and dbt, with retries and failure alerts
- [ ] Docker setup
- [ ] CI with GitHub Actions (pytest + dbt build on every PR)
- [ ] Infrastructure as code (Terraform), later

## Status
🚧 In progress
