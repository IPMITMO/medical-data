require 'rubygems'
require 'bundler/setup'
require 'sinatra/base'
require 'pg'
require 'json'

@dbconfig = {
    host: 'localhost',
    port: 5432,
    dbname: 'meddata',
    user: 'postgres',
    options: nil,
    tty: nil,
    password: ''
}

class MedDataApi < Sinatra::Base
  set :public_folder, File.dirname(__FILE__)

  def db
    PGconn.connect('localhost', 5432, nil, nil, 'meddata', 'meddata', 'meddata')
  end

  get '/' do
    File.read(File.join('./', 'index.html'))
  end

  get '/data' do
    db.exec('SELECT * FROM data').to_a.to_json
    # 'test'
  end

end



