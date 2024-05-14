DOCKER_RUN=docker run --rm --volume .:/app -w /app -it event-menu-web-menu

install:
	$(DOCKER_RUN) npm i $(PACKAGE)

build:
	VITE_API_URL=https://cardapio.fernandohtr.com npm run build
