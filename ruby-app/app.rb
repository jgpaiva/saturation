require 'sinatra'
configure { set :server, :puma }

get '/hello' do
  "Hello World!"
end
