#List of destinations our users frequent
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

#test object that shows the list order
test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#Function that retrieves the index of the destination from the destinations list
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#print(get_destination_index("Hyderabad, India"))

#Function that takes the index from the traveler object. Uses the [1] index as that's where the destination lies in the user's traveler card.
def get_traveler_location(traveler):
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index

#Tests the get_traveler_location function and retrieves 1 as that's where Shanghai (the test_traveler's destination) is in the destinations list.
test_destination_index = get_traveler_location(test_traveler)
#print(test_destination_index)

#Variable that creates an attraction list for each destination
attractions = [[] for destination in destinations]
#print(attractions)

#Function creates a list of attractions for the specified destinaion if the destination is already listed in destinations.
def add_attraction(destination, attraction):
  try:
    destination_index = get_destination_index(destination)
    attractions_for_destination = attractions[destination_index].append(attraction)
    return attractions_for_destination
  except ValueError:
    return
  
#Adding attractions with the add_attraction function
add_attraction("Los Angeles, USA",['Venice Beach', ['Beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city = attractions[destination_index]
  attractions_with_interest = []
    