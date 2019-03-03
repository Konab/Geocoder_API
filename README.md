# Geocoder_API

Geocoder_API is a simple python library that provides access to the geodata service with functionality:

* Get address by geo-point
* Get nearest geo-point to the road
* Find the distance between the points
* Find the specific geo-point using a unique algorithm

## History
On the hackathon PublicData implemented an algorithm for finding the correct geo-points of traffic collisions from unreliable geodata. We implemented geocoder and started the service with unique algorithm for finding corrective points. This library allows everyone to use our unique algorithm and our geocoder.

## Tech
We import downloaded OSM dataset into PostgreSQL, write geocoding functions and the unique algorithm in PL/pgSQL. Implemented API to these functions by URL queues.

File geocoder_51c.py stores the class Geocoder_51c with methods for work with the API service. Below is a detailed description of each **method**:

### get_address_point
```
Returns the geo-point of the address
Arguments:
  n_p {str} -- name of the settlement
  street {str} -- name of the street
  house {str} -- house number
Returns:
  [json] -- Geo-data
```
### get_diapason
```
Checks if point №2 is within the range of 300 meters from point №1
Arguments:
  point_1 {str} -- geo-data
  point_2 {str} -- geo-data
```
### get_closest_point_on_road
```
Returns the projection of the building to the road
Arguments:
  n_p {str} -- name of the settlement
  street {str} -- name of the street
  house {str} -- house number
Returns:
  [json] -- Geo-data
```
### get_closest_point_on_road
```
Returns the calculated point
Arguments:
  n_p {str} -- name of the settlement
  street {str} -- name of the street
  house {str} -- house number
  dtp_point {str} -- geo-point
Returns:
  [json] -- Geo-data
```
