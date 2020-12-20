# WhatAPhish: Detecting Phishing Website
Website Phishing costs internet users billions of dollars per year. Phishers steal personal information and financial account details such as usernames and passwords, leaving users vulnerable in the online space. Traditionally, the ad-hoc methods have been used to detect phishing attacks based on content, URL of the webpage, etc. It is difficult to detect phishing websites because of the use of URL obfuscation to shorten the URL, link redirections and manipulating link in such a way that it looks trustable. We present a machine learning based approach combining several features to attain the best results. Among various classification models, Random Forest Classifier and Support Vector Machine were able to classify most accurately with least number of false positives. After analysing, we used SVM which achieved an accuracy of 96.29% on test data and 97.95% on training data with a set of 25 features spanning over broad categories of URL parsing, pages’ source code and URLs embedded therein and domain based statistics. We then created a web-platform WhatAPhish to deploy the obtained results.

# User Interface
![complete](https://user-images.githubusercontent.com/43923076/102724382-39fad680-4335-11eb-84e9-f619deb447f6.png)

# Detecting Phishing Website
![phi](https://user-images.githubusercontent.com/43923076/102724562-767b0200-4336-11eb-9e1d-6afad20a0c2a.png)

# Detecting Legitimate Website

# Conclusion
In this project, we built WhatAPhish - a mechanism to detect phishing websites. Our methodology uses not just traditional URL based or content based rules but rather employs the machine learning technique to identify not so obvious patterns and relations in the data. We have used features from various domain spanning from URL to HTML tags of the webpage, from embedded URLs to favicon, and databases like WHOIS, Alexa, Pagerank, etc. to check the traffic and status of the website. We were able to obtain an accuracy of more than 96\%, recall greater than 96\% with a False Positive Rate of less than 5\%, thus classifying most websites correctly and proving the effectiveness of the machine learning based technique to attack the problem of phishing websites. We provided the output as a user-friendly web platform whch can futher be extended to a browser extension to provide safe and healthy online space to the users.
