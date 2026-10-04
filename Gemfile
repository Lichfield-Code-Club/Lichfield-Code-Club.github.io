source "https://rubygems.org"

gem "jekyll", "~> 3.9"

gem "minima"
gem "faraday-retry"
gem "kramdown-parser-gfm"
gem "webrick", "~> 1.8"

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
end

install_if -> { RUBY_PLATFORM =~ %r!mingw|mswin|java! } do
  gem "tzinfo", "~> 2.0"
  gem "tzinfo-data"
end
