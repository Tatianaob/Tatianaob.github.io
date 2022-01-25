# A function using tuples to see how many countries I visited from 2015 to 2021

def get_data(Trips):
  nums = ()
  words = ()
  for i in Trips:
    nums = nums + (t[0],)
    if t[1] not in words:
      words = words + (t[1],)
  min_n = min(nums)
  max_n = max(nums)
  unique_words = len(words)
  return (min_n, max_n, unique_words)

tatiana = ((2015, "Argentina"),
           (2016, "USA"),
           (2017, "Canada"),
           (2018, "Colombia"),
           (2019, "Jordan"),
          (2021, "Mexico"),
          )
(min_year, max_year, num_countries) = get_data(tatiana)
print("From", min_year, "to", max_year, \
      "Tatiana visited", num_countries, "countries".)
      
