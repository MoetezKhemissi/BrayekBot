

## Step 1: Update and Install Dependencies
sudo apt-get install -y git python3 python3-venv python3-pip xvfb wget

## Step 2: Clone the Repository
git source venv/Scripts/activate

## Step2.2:Virtual display go brrr
sudo apt-get install xvfb -y

## Step 3: activate Python Virtual Environment
./venv/Scripts/activate

## Step 4: Install Python Packages
pip install -r requirements.txt
pip install pyvirtualdisplay undetected-chromedriver

## Step 5: Install Google Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install -y ./google-chrome-stable_current_amd64.deb

## Step 6: Run the Project
python3 main.py

## Config: 
test.txt contains emails 
result.csv is actual result
config file can change higher wait times ( for bad internet times)
## Ps: 
some lines will be duplicated with unkown then found/not found ignore it for now too lazy to make post-process script to remove these dupes