require 'pg'

def db
  PGconn.connect('localhost', 5432, nil, nil, 'meddata', 'meddata', 'meddata')
end

@db = db

area, street, id_exitus, id_prvs, main, mkb = {}, {}, {}, {}, {}, {}

# area
area_raw = File.open('raw/area.csv').readlines
area_raw.map{ |item| area[item.split(";")[1]] = {
      name: item.split(";")[2],
      lat: item.split(";")[3],
      lon: item.split(";")[4].delete("\n")
  }
}
area.delete "IDENT"

# street
street_raw = File.open('raw/street.csv').readlines
street_raw.map{ |item| street[item.split(";")[1]] = item.split(";")[2].delete!("\n") }
street.delete "IDENT"

# id_exitus
id_exitus_raw = File.open('raw/id_exitus.csv').readlines
id_exitus_raw.map{ |item| id_exitus[item.split(";")[1]] = item.split(";")[2].delete!("\n") }
id_exitus.delete "ABBREVIATION"

# id_exitus
id_prvs_raw = File.open('raw/id_prvs.csv').readlines
id_prvs_raw.map{ |item| id_prvs[item.split(";")[1]] = item.split(";")[2].delete!("\n") }
id_prvs.delete "CODE"

# id_exitus
mkb_raw = File.open('raw/mkb.csv').readlines
mkb_raw.each{ |item| mkb[item.split(";")[0]] = item.split(";")[1] }

main_raw = File.open('raw/main.csv').readlines
# main_raw = main_raw[1..20].map{|item| item.split(";")}
main_raw = main_raw.map{|item| item.split(";")}

main = main_raw.each do |item|
  # printf "%-20s %-2s\t%-20s\t%-80s\t%-20s\n", item[1], item[2], street[item[3]], mkb[item[7]], id_prvs[item[10]], id_exitus[item[10]]
  # puts(item[5])

  area_name = area[item[5]] ?  area[item[5]][:name] : ''
  area_lat = area[item[5]] ?  area[item[5]][:lat].to_f : nil
  area_lon = area[item[5]] ?  area[item[5]][:lon].to_f : nil
  @db.exec_params('INSERT INTO meddata (date, area_name, area_lat, area_lon, street, mkb, prvs, exitus) VALUES ($1, $2, $3, $4, $5, $6, $7, $8)', [
      item[1], area_name, area_lat.to_f, area_lon, street[item[3]], mkb[item[7]], id_prvs[item[10]], id_exitus[item[10]]
  ])
  # printf "%s;%s;%s;%s;%s;%s;%s;%s\n", item[1], area_name, area_lat, area_lon, street[item[3]], mkb[item[7]], id_prvs[item[10]], id_exitus[item[10]]
end
