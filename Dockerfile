FROM --platform=linux/arm64 public.ecr.aws/lambda/python:3.11

RUN pip install poetry && pip install poetry-plugin-export

COPY src/ ${LAMBDA_TASK_ROOT}/src/
COPY poetry.lock pyproject.toml ./

RUN poetry export -f requirements.txt -o requirements.txt --without-hashes
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

ENV LD_PRELOAD /var/task/sklearn/utils/../../scikit_learn.libs/libgomp-d22c30c5.so.1.0.0

CMD ["src.main.handler"]
