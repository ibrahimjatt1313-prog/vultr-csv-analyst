FROM python:3.10-slim
WORKDIR /workspace
RUN pip install --no-cache-dir pandas matplotlib seaborn plotly
RUN useradd -ms /bin/bash sandboxuser
USER sandboxuser
CMD ["python"]