FROM mcr.microsoft.com/devcontainers/ruby:1-3.2-bookworm

RUN gem update --system \
    && gem install bundler -v 2.5.23 --no-document \
    && bundle _2.5.23_ --version

WORKDIR /workspaces/open-horizon.github.io
