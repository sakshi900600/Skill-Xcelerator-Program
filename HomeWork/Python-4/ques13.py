# Replace Special Terms with Definitions 

# output:  "a process in plants happens in a green pigment using sunlight"


definitions = { 
  "Photosynthesis": "a process in plants", 
  "chlorophyll": "a green pigment" 
}

text = "Photosynthesis happens in chlorophyll using sunlight" 

words = text.split()

result = []

for word in words:
    if definitions.get(word):
      result.append(definitions.get(word))
    else:
       result.append(word)
    

ans = " ".join(result)
print(ans)


