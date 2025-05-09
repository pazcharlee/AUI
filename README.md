# Adaptive User Interface (AUI) - Context-Aware Login System
Author: Charlee Paz

## Overview
This project focuses on building an Adaptive User Interface (AUI) designed to enhance cybersecurity by responding intelligently to simulated user behavior during login attempts. Rather than relying on static security measures, the AUI dynamically adjusts its prompts based on predefined conditions that simulate anomalous behaviors, such as unusual login times or repeated failed attempts.

While the system is not yet adapted to track actual individual user behavior, it mimics realistic patterns of login activity through these simulated conditions. This allows for an exploration of how adaptive, context-aware security interfaces can defend against social engineering threats, particularly in the evolving landscape shaped by generative AI.

## Features
### Context-Aware Security Prompts:
Triggers additional security questions when login behavior deviates from simulated normal patterns (e.g., logging in during unusual hours, or after failed login attempts). These conditions are predefined to simulate the types of behavior that could indicate a potential security threat.

### Real-Time Adaptivity:
Adjusts responses based on the simulated user activity, offering flexibility without overwhelming or overcomplicating the user experience.

### Speed and Accuracy:
Achieved a response time between 0.7692 and 0.8414 seconds and a 100% success rate in simulated scenarios.

### Focus on User Engagement:
Encourages active participation by the simulated user without creating alert fatigue or over-reliance.

### How to Use
To run the program, execute the Python script **Budgetly1.py**. You can do this by following these steps:

1. Make sure you have Python installed on your system.
2. Open a terminal or command prompt.
3. Navigate to the directory where Budgetly1.py is located.
4. Install the required libraries by running the following command:
             **pip install -r requirements.txt**

This will install all the dependencies listed in the requirements.txt file.
After the libraries are installed, run the script using the following command:
              **python Budgetly1.py**
