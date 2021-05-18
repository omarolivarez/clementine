# clementine
A sleek desktop app for processing heavy bootstrapping loads.  
**Version:** 1.0  
**Stack:** Python, Eel, HTML, Javascript, CSS  

## Issue being solved
I can't run my laptop while charging it at the same time. That means, if I ever have to run a computation for a very long time, there's a risk that my laptop will run out of battery and lose its work before the computation is complete. There's nothing worse than having to start that work all over again.  
<br />
On a recent project, I was bootstrapping a dataset of more than a million rows. It became too much for my laptop to handle - quickly heating up and draining my laptop's battery at only 1,000 bootstrap repetitions. I created **Clementine** to solve this problem.  

## Solution
1. First, Clementine provides a graphical user interface for you to execute bootstrapping. No need to mess around with R or pandas when you've got Clementine lifting that heavy load on the backend for you. Clementine runs on the Eel framework which leverages the Chrome browser for a sleek, familiar interface. Please, let's bring the UIs for our apps into the 21st century.   
2. Clementine stores your bootstrapped statistic on a fast, local database. That means your data is securely stored on your local machine. It also means that if you need to pause your bootstrapping (because your battery is running out), you can easily pick up where you left off by reading your locally stored data after your battery is charged.

## Feedback welcome!
I would love to improve Clementine for the scientific and developer communities. Have any recommendations, feature requests, or bug fixes? Please reach out to me and I'd be happy to incorporate your feedback.
