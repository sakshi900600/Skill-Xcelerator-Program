# Print player names who scored above 50.

# Output: ['Gill', 'Kohli', 'Pant']
scores = { 
    'Gill': 52, 
    'Kohli': 90, 
    'Dhawan': 38, 
    'Pant': 64 
}

for name,score in scores.items():
    if score > 50:
        print(name)