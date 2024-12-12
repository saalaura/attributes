#nominal attributes
print("These are the nominal attributes: ")
print(["show id", "type", "title", "release_year", "listed_in", "rating"])
#binary attributes
print("There are no binary attributes here in our dataset.")
#ordinal attributes
print("The ordinal attribute in out dataset is: ")
print(df['release_year'].value_counts())
print("Release year is an ordinal attribute since it can be put in an order among it's own group")
