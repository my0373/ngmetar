FROM soleng.jfrog.io/matthewy-ci-containers/python:3
ARG PYPI_REPO_VAR
RUN mkdir -p /app/
COPY ../* /app
WORKDIR /app
RUN ls -l .
RUN echo "Log ${PYPI_REPO_VAR}"
RUN pip install -r ./requirements.txt --extra-index-url=${PYPI_REPO_VAR}
      
# RUN pipenv install --extra-index-url=${PYPI_REPO_VAR}
# RUN pipenv install --system --deploy --extra-index-url=${PYPI_REPO_VAR}
CMD ["python", "metar.py"]