#colors 
green = \x1B[0;32m
red = \x1B[0;31m
yellow = \x1B[0;33m
cyan = \x1B[0;36m
no_color = \x1B[0m

#Commands variables 
JEKYLL=bundle exec jekyll
BUNDLE=bundle 
GEM=gem install bundler

# default command/output 
default: show-args

# default output in user just type "make"
show-args: 
	@echo "${cyan} FOLLOW THESE INSTRUCTIONS${no_color}"
	@echo "${cyan} make init: ${green}install and update all dependencies. run once before using tools each day${no_color}"
	@echo "${cyan} make run: ${green}start the local web server. does not build the site first.${no_color}"
	@echo "${cyan} make dev: ${green}build and test the local documentation site${no_color}"
	@echo "${cyan} make build: ${green}build the local documentation site. typically done before "make run"${no_color}"
	@echo "${cyan} make test: ${green}test the local documentation site${no_color}"


# make init: install and update all dependencies. run once before using tools each day
init:
	$(GEM)
	$(BUNDLE) update --bundler
	$(BUNDLE) config set --local deployment 'true'
	$(BUNDLE) install

#  make run: start the local web server. does not build the site first. 
run:
	$(JEKYLL) serve

# make dev: build and test the local documentation site 
dev: 
	$(JEKYLL) build
	$(JEKYLL) serve
	$(JEKYLL) doctor

# make build: build the local documentation site. typically done before "make run"
build:
	$(JEKYLL) build

# make test: test the local documentation site
test: 
	$(JEKYLL) doctor

# These special targets are called "PHONY", These targets explicitly tell Make they're not associated with files
.PHONY : default init run dev build test