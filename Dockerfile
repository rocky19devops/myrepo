FROM alpine
WORKDIR /app
COPY rocky.sh .
ENTRYPOINT [ "/bin/sh" ]
CMD [ "rocky.sh" ]
