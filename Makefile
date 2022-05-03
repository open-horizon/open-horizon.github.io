# Command variables 
JEKYLL=bundle exec jekyll
BUNDLE=bundle 
GEM=gem install bundler

# default command/output 
default: show-args

# default output in user just type "make"
show-args: 
	@echo Follow these instructions:
	@echo make init: Install and update all dependencies., and run one time before using the tools each day
	@echo make run: start the local web server. does not build the site first.
	@echo make dev: build and test the local documentation site
	@echo make build: build the local documentation site. typically done before "make run"}
	@echo make test: test the local documentation site


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

# These special targets are referred to as PHONY, which explicitly tells the make file that they are not associated with files.
.PHONY : default init run dev build test