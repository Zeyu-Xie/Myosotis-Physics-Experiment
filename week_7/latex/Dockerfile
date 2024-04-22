FROM acanxie/xelatex:1.0.0

WORKDIR /app

COPY . /app

RUN chmod +x /app/compile.sh

CMD ["bash", "./compile.sh"]