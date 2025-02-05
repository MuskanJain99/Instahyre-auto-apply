# **Instahyre Auto Apply Bot**  
A **Python-based Selenium bot** that automates job applications on [Instahyre](https://www.instahyre.com). It logs in using stored credentials, filters jobs based on user-defined preferences, and applies to available job listings automatically.  

---

## **✨ Features**  
✅ Logs in automatically using credentials stored in a `.env` file.  
✅ Selects desired job functions based on user input.  
✅ Applies to jobs automatically.  

---

## **⚙️ Installation**  

### **🛠 Prerequisites**  
Ensure you have the following installed:  
- **[Python 3](https://www.python.org/downloads/)**  
- **[Google Chrome](https://www.google.com/chrome/)**  
- **[Chrome WebDriver](https://chromedriver.chromium.org/downloads)**  

---

## **📝 Setup**  

1. **Clone this repository:**  
   ```bash
   git clone https://github.com/your-username/instahyre-auto-apply.git
   cd instahyre-auto-apply

2. **Install dependencies:**  
   ```bash
   pip install -r requirements.txt

3. **Create a .env file:**
   In the project directory, create a .env file and add your Instahyre credentials and desired job functions:
   ```bash
   INSTA_EMAIL=your-email@example.com
   INSTA_PASSWORD=yourpassword
   DESIRED_OPTIONS=Software Development, Data Science

4. **Run the script:**
   ```bash
   python main.py

## **🚀 Usage**
Once the script is running, it will:

Log in to Instahyre using the credentials provided in the .env file.

Filter job listings based on the DESIRED_OPTIONS specified.

Automatically apply to the available job listings.

Enjoy automated job applications! 🚀
   
