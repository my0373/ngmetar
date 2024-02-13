# This first argument can only be used for the "FROM" line
# EXAMPLE:

ARG BASE_IMAGE
FROM ${BASE_IMAGE}

# Arguments used within the dockerfile
ARG PYPI_REPO_VAR

# Create a working directory for the code
RUN mkdir -p /metarng/

# Copy repository code in from the root directory
COPY ../* /metarng

# Set the metarng folder the working directory from here on.
WORKDIR /metarng

RUN ls -l .
RUN echo "Log ${PYPI_REPO_VAR}"

# Install the python requirements from the specified repo
RUN pip install -r ./requirements.txt --extra-index-url=${PYPI_REPO_VAR}


# Run python command python metar.py
CMD ["python", "metar.py"]