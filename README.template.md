<!-- BADGES -->
[contributors_badge]: https://img.shields.io/github/contributors/{{github_username}}/{{repository_name}}.svg?style=for-the-badge
[contributors_url]: https://github.com/{{github_username}}/{{repository_name}}/graphs/contributors
[forks_badge]: https://img.shields.io/github/forks/{{github_username}}/{{repository_name}}.svg?style=for-the-badge
[forks_url]: https://github.com/{{github_username}}/{{repository_name}}/network/members
[stars_badge]: https://img.shields.io/github/stars/{{github_username}}/{{repository_name}}.svg?style=for-the-badge
[stars_url]: https://github.com/{{github_username}}/{{repository_name}}/stargazers
[issues_badge]: https://img.shields.io/github/issues/{{github_username}}/{{repository_name}}?style=for-the-badge
[issues_url]: https://github.com/{{github_username}}/{{repository_name}}/issues
[license_badge]: https://img.shields.io/github/license/{{github_username}}/{{repository_name}}.svg?style=for-the-badge
[license_url]: https://github.com/{{github_username}}/{{repository_name}}/blob/master/LICENSE.txt
[linkedin_badge]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin_url]: https://linkedin.com/in/{{linkedin_username}}

<!-- TECHNOLOGY BADGES -->
[python_badge]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[python_url]: https://www.python.org/
[fastapi_badge]: https://img.shields.io/badge/FastAPI-0056B3?style=for-the-badge&logo=fastapi&logoColor=white
[fastapi_url]: https://fastapi.tiangolo.com/
[docker_badge]: https://img.shields.io/badge/Docker-2CA5E0?style=for-the-badge&logo=docker&logoColor=white
[docker_url]: https://www.docker.com/
[kubernetes_badge]: https://img.shields.io/badge/kubernetes-326CE5?style=for-the-badge&logo=kubernetes&logoColor=white
[kubernetes_url]: https://kubernetes.io/
[gitlab_badge]: https://img.shields.io/badge/gitlab-326CE5?style=for-the-badge&logo=gitlab&logoColor=white
[gitlab_url]: https://gitlab.com/
[github_badge]: https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white
[github_url]: https://github.com/
[grafana_badge]: https://img.shields.io/badge/grafana-F46800?style=for-the-badge&logo=grafana&logoColor=white
[grafana_url]: https://grafana.com/
[prometheus_badge]: https://img.shields.io/badge/prometheus-E6522C?style=for-the-badge&logo=prometheus&logoColor=white
[prometheus_url]: https://prometheus.io/

<!-- README -->
<a id="readme-top"></a>

# {{project.name}}

[![Contributors][contributors_badge]][contributors_url]
[![Forks][forks_badge]][forks_url]
[![Stargazers][stars_badge]][stars_url]
[![Issues][issues_badge]][issues_url]
[![MIT License][license_badge]][license_url]

<br />
**Built with** [![Python][python_badge]][python_url] [![Docker][docker_badge]][docker_url] [![FastAPI][fastapi_badge]][fastapi_url] [![Kubernetes][kubernetes_badge]][kubernetes_url] [![GitHub][github_badge]][github_url] [![Grafana][grafana_badge]][grafana_url] [![Prometheus][prometheus_badge]][prometheus_url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/{{github_username}}/{{repository_name}}">
    <img src="{{project.logo}}" alt="Logo" width="150" height="150">
  </a>
</div>

<!-- PROJECT DESCRIPTION -->
<p align="center" style="font-size: 1.2rem; font-weight: 300; color: #666;">
  {{project.description}}
</p>

<!-- PROJECT INFO -->
<div>
  <p align="center">
    <br />
    <a href="https://github.com/{{github_username}}/{{repository_name}}/blob/main/docs/README.md"><strong>Explore the docs</strong></a>
    <br />
    <br />
    <a href="{{demo_url}}">View Demo</a>
    ·
    <a href="https://github.com/{{github_username}}/{{repository_name}}/issues/new?labels=bug&template=bug-report---.md">Report Bug</a>
    ·
    <a href="https://github.com/{{github_username}}/{{repository_name}}/issues/new?labels=enhancement&template=feature-request---.md">Request Feature</a>
  </p>
</div>


## Table of Contents

<details>
  <summary>Click to expand</summary>
  <ol>
    <li><a href="#about-the-project">About The Project</a>
    </li>
    <li><a href="#key-features">Key Features</a></li>
    <li><a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#configuration">Configuration</a></li>
        <li><a href="#installation">Installation</a></li>
        <li><a href="#usage">Usage</a></li>
      </ul>
    </li>
    <li><a href="#known-issues">Known Issues</a></li>
    <li><a href="#development">Development</a></li>
    <li><a href="#security--privacy">Security & Privacy</a></li>
  </ol>
</details>

## About The Project

POC of a Salary Prediction API including ETL pipeline, Machine Learning (simplified) and a Kubernetes deployment through a whole CI/CD pipeline.


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Key Features

    ### 📊 Machine Learning
    - **Linear Regression**: Simple model to predict salary based on features
    - **Data Preprocessing**: Transformations to prepare data for model training
    - **Model Evaluation**: Metrics to evaluate model performance
    - **Model Persistence**: Save and load trained models

    ### 📊 Data Processing
    - **Data Extraction**: Download data from a URL and save it to a file
    - **Data Transformation**: Transform the data into a DataFrame

    ### 📊 CI/CD
    - **GitHub Actions**: CI/CD pipeline for building and deploying the application
    - **Docker**: Containerization for deploying the application
    - **Kubernetes**: Container orchestration for deploying the application

    ### 📊 Monitoring
    - **Grafana**: Monitoring for visualizing the data
    - **Prometheus**: Metrics for monitoring the application

<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Getting Started

### Prerequisites
- **Python 3.12+** with [uv](https://github.com/astral-sh/uv) package manager
- **Docker & Docker Compose** for infrastructure services
- **Kubernetes** for deployment


### Installation
1. **Clone the repository**
   ```bash
   git clone https://github.com/{{github_username}}/{{repository_name}}.git
   cd {{repository_name}}
   ```
2. **Install dependencies**
   ```bash
   uv sync
   ```

### Usage
- You can directly use the API to get predictions.

*Examples*

```bash
curl -X 'POST' \
  'http://localhost:8000/predict' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "company": 0,
  "gender": 0,
  "position_level": 0,
  "performance_score": 0,
  "work_hours_per_week": 0,
  "experience_years": 0,
  "has_certifications": true,
  "promoted": true
}'
```


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Known Issues

- [ ] 



## Development

### Project structure

```text
salary_analysis_infrastructure/
├── documents/
│   └── changelogs/
│       └── 1.0.0.md                   # Version changelog
├── scripts/
│   ├── api_test.sh                    # API testing script
│   ├── config.json                    # README generation configuration
│   └── generate_readme.py             # README template processor
├── src/
│   ├── api/
│   │   ├── build_image.sh             # Docker image build script
│   │   ├── Dockerfile                 # API container definition
│   │   ├── main.py                    # FastAPI application
│   │   ├── requirements.txt           # API dependencies
│   │   └── run_container.sh           # Container execution script
│   ├── docker/
│   │   ├── build_model/
│   │   │   ├── build_model.py         # Model training service
│   │   │   ├── Dockerfile             # Model builder container
│   │   │   └── requirements.txt       # Model builder dependencies
│   │   ├── docker-compose.yml         # Multi-service orchestration
│   │   └── prepare_dataframe/
│   │       ├── Dockerfile             # Data preparation container
│   │       ├── prepare_dataframe.py   # Data preprocessing service
│   │       └── requirements.txt       # Data preparation dependencies
│   ├── kubernetes/
│   │   ├── api_deploy.yml             # API deployment configuration
│   │   ├── api_svc.yml                # API service configuration
│   │   ├── create_config_map.sh       # ConfigMap creation script
│   │   ├── create_namespace.sh        # Namespace creation script
│   │   ├── models_pv.yml              # Persistent volume for models
│   │   ├── models-pvc.yml             # Persistent volume claim
│   │   └── secret_container_registry.sh # Container registry secrets
│   ├── monitoring/
│   │   └── docker-compose.yml         # Monitoring stack (Grafana/Prometheus)
│   └── pipeline/
│       ├── build_model.py             # ML model training pipeline
│       ├── extract.py                 # Data extraction from sources
│       ├── prepare_dataframe.py       # Data preprocessing pipeline
│       └── transform_json_to_csv.py   # Data format transformation
├── tests/
│   ├── conftest.py                    # pytest configuration
│   └── model_test.py                  # Model validation tests
├── LICENSE                            # MIT License
├── pyproject.toml                     # Python project configuration
├── README.template.md                 # README template
└── uv.lock                            # Dependency lock file
```



### Changelogs

- [V1.0.0](documents/changelogs/1.0.0.md) - Initial release


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## Security & Privacy

- **🔐 No Personal Data Storage**: The whole data pipeline use public data.
- **🏠 Local Storage**: All data is stored locally by default


<p align="right">(<a href="#readme-top">back to top</a>)</p>


## License

Distributed under the **MIT License**. See `LICENSE.txt` for more information.