require 'rubygems'
require 'bundler/setup'
require 'sinatra/base'
require 'pg'
require 'json'

# @TODO Split sinatra app on multiple files
# http://stackoverflow.com/questions/5015471/using-sinatra-for-larger-projects-via-multiple-files

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
    db.exec('
      select count(m.*), m.area_lat, m.area_lon, m.area_name, array_agg(DISTINCT prvs) as prvs
      from meddata m
      where
        area_lat != 0
      group by area_name, area_lat, area_lon, area_name;'
    ).to_a.map do |e|
      {
          count: e['count'].to_f,
          lat: e['area_lat'].to_f,
          lon: e['area_lon'].to_f,
          area_name: e['area_name'],
          prvs: e['prvs']
      }
    end.to_json
  end

  get '/ping' do
    'PONG ' + params.to_json
  end

end



