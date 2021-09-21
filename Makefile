build:
	docker build -t ${USER}/${shell basename -s .git `git config --get remote.origin.url`}:${shell git branch --show-current} .

run:
	docker run -it ${USER}/${shell basename -s .git `git config --get remote.origin.url`}:${shell git branch --show-current}