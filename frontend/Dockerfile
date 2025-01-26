FROM python:3.12-slim 

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app


COPY ["pyproject.toml","./"]

COPY ["*.py","./"]



RUN uv pip install -r pyproject.toml --system

EXPOSE 8501



ENTRYPOINT ["uv", "run" ,"streamlit" ,"run" ,"app.py"]

