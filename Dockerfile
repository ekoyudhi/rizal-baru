FROM python:3.10.8-alpine
ENV APP_DIR=/opt/otree
RUN mkdir -p ${APP_DIR}
ADD . ${APP_DIR}
RUN pip install --no-cache-dir -r ${APP_DIR}/requirements.txt
EXPOSE 80
WORKDIR ${APP_DIR}
CMD [ "/usr/local/bin/otree", "runprodserver" ]