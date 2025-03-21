### **Deploy Your Flask Web App on PythonAnywhere**  

Since your code is now updated on PythonAnywhere, follow these steps to set up the web app:

---

### **1. Install Dependencies**
1. Open a **Bash console** in PythonAnywhere.  
2. Navigate to your project folder:  
   ```bash
   cd content-generator  # Adjust if needed
   ```
3. Activate the virtual environment (if you created one):  
   ```bash
   source assets/env/bin/activate
   ```
4. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

---

### **2. Set Up the Web App**
1. Go to **PythonAnywhere Dashboard > Web**  
2. Click **Add a new web app**  
3. Select:
   - **Manual configuration**  
   - **Flask**  
   - **Your Python version**  

---

### **3. Configure WSGI File**
1. Click on your web app in the **Web** tab.  
2. Find the **WSGI configuration file** path (e.g., `/var/www/yourusername_wsgi.py`).  
3. Click to **edit** it and replace its contents with:

   ```python
   import sys
   import os

   # Add your project directory to sys.path
   project_home = "/home/yourusername/content-generator"
   if project_home not in sys.path:
       sys.path.insert(0, project_home)

   # Set the Flask app path
   from upload import app as application
   ```

---

### **4. Reload Your Web App**
1. Go to the **Web** tab.  
2. Click **Reload** on your web app.  

Your Flask app should now be running on **`yourusername.pythonanywhere.com`**! 🚀  

---

### **Next Steps**
- Test the upload and download functionality.  
- Let me know if anything needs debugging! 🔥