FROM python:3.12-slim 

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app


COPY ["pyproject.toml","./"]

COPY ["/artifacts","./artifacts"]


COPY ["*.py","./"]

COPY  ["*.bin","./artifacts"]

RUN uv pip install -r pyproject.toml --system


RUN uv pip install -e . --system


EXPOSE 5000
EXPOSE 8501


RUN uv run fastapi run server --host '0.0.0.0' --port 5000 


ENTRYPOINT [ "uv","run","streamlit","run","app.py"] 
# ["fastapi", "run", "--host", "0.0.0.0", "--port", "5000"]