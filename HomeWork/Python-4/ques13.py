# Replace Special Terms with Definitions 

# output:  "a process in plants happens in a green pigment using sunlight"


definitions = { 
  "Photosynthesis": "a process in plants", 
  "chlorophyll": "a green pigment" 
}

text = "Photosynthesis happens in chlorophyll using sunlight" 

text = text.split()

for name, defi in definitions.items():
    if name in text:
        text.remove(name)
        text.append(defi)

print(text)
    


