pushd _data
rm -rf *.*json
popd
python gc.py
pushd _data
python teste.py
popd
python3 hdbosm.py
python hdb2d.py

ogr2ogr -f "GeoJSON" _data/footprints_r.geojson _data/footprints.geojson -s_srs EPSG:4326 -t_srs EPSG:3414

python3 hdb3d.py

