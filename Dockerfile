FROM python:3.12-slim 

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

# Change the working directory to the `app` directory
WORKDIR /app

COPY ["requirements.txt","./"]

COPY ["pyproject.toml","./"]

COPY ["/artifacts","./artifacts"]


COPY ["*.py","./"]

COPY  ["*.bin","./artifacts"]

RUN uv pip install -r pyproject.toml --system


RUN uv pip install -e . --system


EXPOSE 5000

# RUN source /.venv/bin/activate


ENTRYPOINT ["fastapi", "run", "--host", "0.0.0.0", "--port", "5000"]