from sklearn import tree

features = [
    [140, 1], 
    [130, 1], 
    [150, 0],  
    [170, 0],  
]
labels = [0, 0, 1, 1]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(features, labels)

mystery_fruit = [[160, 0]]
prediction = clf.predict(mystery_fruit)

if prediction[0] == 0:
    print("it is an apple!")
else:
    print("it is an orange!")
