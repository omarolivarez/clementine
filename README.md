# clementine
**What is it?** A sleek desktop app for processing heavy bootstrapping loads.  
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

## How to use Clementine  
**What you'll need:** a CSV file that contains a column that you would like to bootstrap.
1. Upon launching Clementine, you will be prompted to select a CSV to process. Navigate to the location of your CSV and click the "Process" button in Clementine.
2. History files are Clementine's way of storing your previous progress. If this is your first time running Clementine, you won't have any history files to upload, and can simply leave the default option of "No" for Import History? In future runs, you can use the option "Yes" to import your progress into Clementine so it can start where you last left off.
3. Clementine will select the column headers for your CSV and display them in the Column field. Select the column you would like to bootstrap. This column must contain numbers as either integers (1, 2, 3) or floats (0.2, 2.1, 3.0).
4. Select which statistic you would like to calculate on each bootstrapped sample. You can select from: Mean, Median  
5. Select how many repetitions you would like Clementine to perform. You can always pause Clementine mid-way through your bootstrapping so it's okay if you want to bootstrap a lot! (10,000 or more)
6. Click the Begin button to launch the bootstrapping process. 

## Screenshots
Configuration screen to prepare bootstrap:
![pre-bootstrap setup](https://github.com/omarolivarez/clementine/blob/main/pre-bs.png)

  
 Bootstrapped results screen:
 ![post-bootstrap results](https://github.com/omarolivarez/clementine/blob/main/post_bs.png)
