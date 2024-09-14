from flask import Blueprint, render_template,request,redirect, url_for, render_template_string
import os
import jsonify
import promt as pt

main = Blueprint('main', __name__)
voicesearch = Blueprint('voicesearch', __name__)
onsubmit = Blueprint('onsubmit', __name__)
waterstress = Blueprint('waterstress', __name__)
growthtrack = Blueprint('growthtrack', __name__)
diseasedetection = Blueprint('diseasedetection', __name__)
environ = Blueprint('environ', __name__)
automated = Blueprint('automated', __name__)
crophealth= Blueprint('crophealth', __name__)
growthprediction = Blueprint('growthprediction', __name__)
marketsales = Blueprint('marketssales', __name__)
supplychain = Blueprint('supplychain', __name__)
automatedtskmange = Blueprint('automatedtskmange', __name__)

global fast 

fast = True

@automatedtskmange.route('/automatedTasksForm')
def automatedtskmange1():
    if fast == True:
        return render_template('automatedtsk.html')
    else:
       #global fullform
       result =  pt.answer(''' most mportant thing is that dont make complex html make simple but better at looking and easyly excutableTask Scheduling Form:

Input fields for task name, description, due date, and due time.
A button to add the task.
Task Table:

A table to display the scheduled tasks with columns for task name, description, due date, due time, and actions (edit/delete).
Notification Section:

A section to display alerts or messages regarding tasks (e.g., task added successfully, errors).
Multilingual Support:

Include options to select preferred language and ensure that all messages and labels adapt to the selected language.
Styling:

Use a dark theme with Bootstrap for styling.
Ensure that the design is clean and user-friendly, with good color contrasts and responsive layout.
JavaScript:

Include JavaScript functionality for dynamically adding tasks to the table and managing notifications.
and make graphs with some fake data'''+fullform)
       return render_template_string(result)



@supplychain.route('/supplyChainForm')
def supplychain1():
    #global fullform
        
    if fast == True:
       return render_template('supplychain.html')
    else:
        
     result =  pt.answer('''Graph Representation:
most mportant thing is that dont make complex html make simple but better at looking and easyly excutable
Use a charting library (e.g., Chart.js) to create a graph that displays supply chain metrics such as:
Total Supply Volume
Distribution Network Efficiency
Transportation Costs
Inventory Levels
Include a dropdown menu to select different metrics for the graph.
Data Table:

Create a table that shows detailed supply chain data, including:
Metric Name
Value
Change Over Time
Ensure the table is sortable by each column.
Preferred Language:

Display all text in the page (labels, headings, etc.) in the user's preferred language.
Full Form and Styling:

Provide full forms for any abbreviations used in the data.
Use Bootstrap for styling to ensure a modern and responsive design.
Include a clean layout with sections for the graph and table.
Interactive Elements:

Add interactive features such as filtering and data sorting.
Include tooltips or modals for additional information on hover.
JavaScript Functionality:

Implement JavaScript to dynamically update the graph and table based on user interactions (e.g., metric selection).
and make graphs with some fake data'''+fullform)


     return render_template_string(result)


@growthprediction.route('/growthPredictionForm')
def growthprediction1():
   # global fullform
       
    if fast == True:
       return render_template('growthprediction.html')
    else:
       result =  pt.answer('''most mportant thing is that dont make complex html make simple but better at looking and easyly excutableCreate an HTML page to represent crop growth data with comprehensive features including tables, graphs, and images. The page should include:

Graphical Representation:

Use a charting library (e.g., Chart.js) to create visualizations of crop growth data. Include:
A line graph showing crop growth over time.
A bar chart comparing growth rates of different crop types.
Provide a dropdown menu to select different crop types or time ranges for dynamic graph updates.
Data Table:

Create a table to display detailed crop growth information, including:
Crop Name
Growth Stage (e.g., Germination, Vegetative, Flowering, Fruiting, Maturity)
Growth Metrics (e.g., Height, Leaf Count)
Date of Observation
Include sorting and filtering options for better data analysis.
Images:

Include a section with images of different growth stages of crops to provide visual context. Use a responsive image gallery or carousel.
Preferred Language:

Ensure all text, labels, and headings are displayed in the user's preferred language.
Full Form and Styling:

Define full forms for any abbreviations used in the data.
Use Bootstrap for modern, responsive styling. Ensure a clean and organized layout with distinct sections for graphs, tables, and images.
Interactive Elements:

Implement JavaScript to enable interactions such as:
Dynamic updates of graphs based on table data or user selection.
Filtering and sorting functionalities for the table.
Image carousel or lightbox for better viewing of crop images.
JavaScript Functionality:

Include JavaScript to handle:
Graph updates in response to user input.
Table sorting and filtering.
Interactive features for the image gallery or carousel.
and make graphs with some fake data
'''+fullform)
    

       return render_template_string(result)


@crophealth.route('/cropHealthForm')
def crophealth1():
   # global fullform
       
    if True:
       return render_template('crophealth.html')
    result =  pt.answer('''most mportant thing is that dont make complex html make simple but better at looking and easyly excutableCreate a comprehensive HTML page to represent crop health data with an engaging and detailed frontend. The page should include:

Crop Health Overview:

A section providing a high-level summary of crop health, including key indicators like overall health status, common issues, and recommendations.
Detailed Health Metrics:

Graphs: Use a charting library (e.g., Chart.js, D3.js) to visualize crop health metrics over time, such as:
A line graph showing changes in health scores or key metrics.
A pie chart or bar chart displaying the distribution of different health issues.
Data Table:

A table displaying detailed crop health data, including:
Crop Name
Health Status (e.g., Healthy, At Risk, Diseased)
Observed Issues (e.g., Pests, Diseases, Nutrient Deficiencies)
Date of Observation
Recommended Actions
Include sorting and filtering options for better data analysis.
Image Gallery:

A section with a gallery or carousel of images depicting various crop health conditions. This can help in visually identifying issues and understanding different stages of crop health.
Alerts and Recommendations:

A notification area for displaying important alerts or recommendations based on the health data. This should include:
Urgent issues requiring immediate attention.
Preventative measures and best practices.
Language Support:

Ensure all text, labels, and headings are in the user’s preferred language. Include a dropdown menu or settings for selecting the preferred language.
Interactive Elements:

Implement interactive features using JavaScript, such as:
Dynamic updates of graphs and tables based on user input or selection.
Filtering and sorting functionalities for the health data table.
Interactive image gallery or lightbox for crop health images.
Styling and Layout:

Use modern CSS frameworks like Bootstrap for a responsive and visually appealing design. Ensure a clean layout with distinct sections for different types of information.
Additional Notes:

Incorporate appropriate icons or images to enhance the visual appeal.
Ensure the page is mobile-friendly and accessible.'''+fullform)
    

    return render_template_string(result)



@marketsales.route('/marketForecastingForm')
def marketsales1():
  #  global fullform
      
    if fast== True:
       return render_template('marketforecast.html')
    else:
     result =  pt.answer('''most mportant thing is that dont make complex html make simple but better at looking and easyly excutableCreate a complete HTML page to represent current market sales data for a crop, using Bootstrap for a modern and responsive design. The page should include:

Page Header:

A header section with the page title, e.g., "Current Market Sales Data" for the selected crop, and a dropdown or selection menu for choosing different crops.
Sales Overview:

A summary section providing a high-level overview of the current market sales, including total sales, average price, and highest and lowest sales figures.
Sales Graphs:

Line Graph: Display a line graph showing sales trends over time (e.g., monthly sales data).
Bar Chart: Include a bar chart to compare sales across different regions or markets.
Data Table:

A detailed table with the following columns:
Market/Region
Sales Volume
Sales Revenue
Average Price
Date of Data
Add sorting and filtering options to make data analysis easier.
Language Support:

Ensure that all text, labels, and headings are in the user’s preferred language. Include a dropdown menu or settings for selecting the preferred language.
Interactive Features:

Graph Interactivity: Allow users to hover over graph data points for additional details.
Table Filtering: Implement table filtering options to view data by date range, market, or crop type.
Styling and Layout:

Utilize Bootstrap's grid system and components to create a responsive layout.
Apply Bootstrap classes for styling graphs, tables, and other elements to ensure a clean and modern appearance.
Additional Features:

Alerts/Notifications: Include an area for important notifications or alerts related to market conditions or trends.
Export Options: Provide buttons for exporting the data as CSV or PDF files for offline analysis.'''+fullform)
    
     return render_template_string(result)



@automated.route('/automatedDataForm')
def automated1():
   # global fullform
       
    if fast == True:
       return render_template('automatedcollection.html')
    else:
      result =  pt.answer('''most mportant thing is that dont make complex html make simple but better at looking and easyly excutableCreate a full HTML page to display automated fake data using Bootstrap for a modern and responsive design. The page should feature:

Page Header:

A header section with the title, e.g., "Automated Data Overview," and a dropdown or selection menu for choosing different data categories.
Data Overview:

A summary section providing a high-level overview of the automated data, including key metrics and statistics.
Graphs and Charts:

Pie Chart: Display a pie chart showing the distribution of different data categories or metrics.
Bar Chart: Include a bar chart to compare values across different categories or time periods.
Data Table:

A detailed table with the following columns:
Category
Metric 1
Metric 2
Metric 3
Date of Data
Add sorting and filtering options for user interaction.
Language Support:

Ensure all text, labels, and headings are in the user’s preferred language. Include a dropdown menu or settings for selecting the preferred language.
Interactive Features:

Chart Interactivity: Allow users to hover over chart elements for additional details.
Table Filtering: Implement filtering options to view data by category or date range.
Styling and Layout:

Use Bootstrap’s grid system and components to create a responsive and attractive layout.
Apply Bootstrap classes for styling charts, tables, and other elements to maintain a clean and modern appearance.
Additional Features:

Alerts/Notifications: Include an area for important notifications or updates related to the automated data.
Export Options: Provide buttons for exporting the data as CSV or PDF files for offline use.and make graphs with some fake data'''+fullform)
    

      return render_template_string(result)



@environ.route('/environmentalImpactForm')
def environ1():
    #global fullform
        
    if fast == True:
       return render_template('envi.html')
    else:
      result =  pt.answer('''most mportant thing is that dont make complex html make simple but better at looking and easyly excutableCreate a full HTML page to represent environmental impact data using Bootstrap for a modern, responsive design. The page should include:

Page Header:

A header section with the title, e.g., "Environmental Impact Overview," and a dropdown menu for selecting different environmental factors or regions.
Impact Overview:

A summary section that provides an overview of key environmental impact metrics, such as emissions, pollution levels, and resource usage.
Graphs and Charts:

Line Chart: Display a line chart showing trends over time for different environmental metrics (e.g., CO2 emissions, water usage).
Bar Chart: Include a bar chart comparing different regions or categories based on their environmental impact.
Data Table:

A detailed table with the following columns:
Region/Category
Emission Levels
Pollution Index
Resource Usage
Date of Data
Add sorting and filtering options for better data analysis.
Language Support:

Ensure that all text, labels, and headings are in the user’s preferred language. Include a dropdown menu or settings for selecting the preferred language.
Interactive Features:

Chart Interactivity: Allow users to hover over chart elements for additional information.
Table Filtering: Implement filtering options to view data by date range or region.
Styling and Layout:

Utilize Bootstrap’s grid system and components to create a responsive and aesthetically pleasing layout.
Apply Bootstrap classes for styling charts, tables, and other elements to ensure a clean and modern appearance.
Additional Features:

Alerts/Notifications: Include an area for important alerts or updates related to environmental impact.
Export Options: Provide buttons for exporting the data as CSV or PDF files for offline access.and make graphs with some fake data'''+fullform)
    
      return render_template_string(result)



@growthtrack.route('/growthTrackingForm')
def growthtrack1():
   # global fullform
   if fast == True:
    return render_template('growthtrack.html')
   else:
   
    result =  pt.answer('''most mportant thing is that dont make complex html make simple but better at looking and easyly excutableCreate a full HTML page to represent crop growth tracking data using Bootstrap for a modern and responsive design. The page should include:

Page Header:

A header section with the title, e.g., "Crop Growth Tracking," and a dropdown menu for selecting different crops or growth stages.
Growth Overview:

A summary section providing an overview of key growth metrics, such as growth stage, plant height, leaf count, and health status.
Graphs and Charts:

Line Chart: Display a line chart showing growth trends over time for metrics like plant height and leaf count.
Bar Chart: Include a bar chart comparing growth metrics across different growth stages or regions.
Growth Data Table:

A detailed table with the following columns:
Growth Stage
Plant Height (cm)
Leaf Count
Health Status
Date of Measurement
Add sorting and filtering options for easier data analysis.
Language Support:

Ensure all text, labels, and headings are in the user’s preferred language. Include a dropdown menu or settings for selecting the preferred language.
Interactive Features:

Chart Interactivity: Allow users to hover over chart elements for additional details.
Table Filtering: Implement filtering options to view data by date range or growth stage.
Styling and Layout:

Utilize Bootstrap’s grid system and components to create a responsive and aesthetically pleasing layout.
Apply Bootstrap classes for styling charts, tables, and other elements to maintain a clean and modern appearance.
Additional Features:

Alerts/Notifications: Include an area for important notifications or updates related to crop growth.
Export Options: Provide buttons for exporting the data as CSV or PDF files for offline use.
Example HTML Code: and make graphs with some fake data'''+fullform)
    

    return render_template_string(result)
    
    
@diseasedetection.route('/diseaseDetectionForm')
def diseasedetection1():
 #   global fullform
     
    if fast == True:
       return render_template('diseasedect.html')
    else:
     result =  pt.answer('''most mportant thing is that dont make complex html make simple but better at looking and easyly excutableCreate a full HTML page to represent disease detection for crops using Bootstrap for a modern and responsive design. The page should include:

Page Header:

A header section with the title, e.g., "Crop Disease Detection," and a dropdown menu for selecting different crops or regions.
Disease Detection Overview:

A summary section providing an overview of detected diseases, including the disease name, affected crop, and severity level.
Disease Images and Details:

Image Upload Section: A section for users to upload images of affected crops for disease detection.
Detected Disease Information: Display information about detected diseases based on uploaded images, including symptoms and recommended treatments.
Graphs and Charts:

Pie Chart: Show the proportion of different diseases detected across various crops or regions.
Bar Chart: Compare the severity of different diseases or the frequency of detection across different crops.
Disease Data Table:

A detailed table with the following columns:
Crop Name
Disease Detected
Severity Level
Date of Detection
Recommended Treatment
Include sorting and filtering options for better data analysis.
Language Support:

Ensure all text, labels, and headings are in the user’s preferred language. Include a dropdown menu or settings for selecting the preferred language.
Interactive Features:

Image Preview: Show a preview of the uploaded image.
Chart Interactivity: Allow users to hover over chart elements for additional details.
Table Filtering: Implement filtering options to view data by date range or disease type.
Styling and Layout:

Utilize Bootstrap’s grid system and components to create a responsive and aesthetically pleasing layout.
Apply Bootstrap classes for styling charts, tables, and other elements to maintain a clean and modern appearance.
Additional Features:

Alerts/Notifications: Include an area for important notifications or updates related to disease detection.
Export Options: Provide buttons for exporting the data as CSV or PDF files for offline use.and make graphs with some fake data'''+fullform)
    

     return render_template_string(result)

@main.route('/')
def home():
    return render_template('index.html')


@onsubmit.route('/submit-farm-data', methods=['POST'])
def submit_farm_data():
    # Get the form data
    global fullform
    language = request.form.get('language')
    crop_type = request.form.get('cropType')
    days_since_planting = request.form.get('daysSincePlanting')
    soil_moisture = request.form.get('soilMoisture')
    irrigation_system = request.form.get('irrigationSystem')
    growth_stage = request.form.get('growthStage')
    disease_symptoms = request.form.get('diseaseSymptoms')
    result = 'Data Submitted !'
    fullform = str(language + crop_type + days_since_planting + soil_moisture + irrigation_system + growth_stage + disease_symptoms )
    
    
    
    return render_template('index.html', result=result)
    

@waterstress.route('/waterStressForm')
def waterstress1():
       if fast == True:
        return render_template('waterstress.html')
       else:
      #  global fullform
         result =  pt.answer('''most mportant thing is that dont make complex html make simple but better at looking and easyly excutableCreate a full HTML page to represent water stress monitoring and smart irrigation using Bootstrap for a clean, responsive design. The page should include:

Page Header:

A header with the title, e.g., "Water Stress Monitoring and Smart Irrigation," and a dropdown menu for selecting different crops or irrigation systems.
Water Stress Overview:

A summary section showing key metrics related to water stress, including soil moisture levels and irrigation system efficiency.
Interactive Form:

Soil Moisture Input: Input field for users to enter the soil moisture percentage.
Irrigation System Selection: Dropdown menu for selecting the type of irrigation system (e.g., Drip, Sprinkler, Manual).
Submit Button: Button to submit the data and view results.
Graphs and Charts:

Line Chart: Display soil moisture levels over time.
Bar Chart: Compare irrigation efficiency across different systems.
Water Stress Data Table:

A table to display the collected data with columns for:
Date
Soil Moisture Level (%)
Irrigation System
Efficiency Rating
Notes
Language Support:

Ensure all text, labels, and headings are in the user’s preferred language. Include a dropdown menu or settings for selecting the preferred language.
Interactive Features:

Chart Interactivity: Allow users to hover over chart elements for additional details.
Table Sorting: Implement sorting options for the data table.
Styling and Layout:

Use Bootstrap’s grid system and components to create a responsive and aesthetically pleasing layout.
Apply Bootstrap classes for styling charts, forms, and tables to maintain a modern appearance.
Additional Features:

Alerts/Notifications: Include an area for displaying alerts or updates related to water stress or irrigation issues.
Export Options: Provide buttons for exporting the data as CSV or PDF files.and make graphs with some fake data'''+fullform)
    

         return render_template_string(result)
    



