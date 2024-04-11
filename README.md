## Cardiovascular Disease Risk Prediction (# Final-Project_Group5)

### Overview
Cardiovascular disease (CVD) poses a significant global health threat, encompassing conditions such as heart disease and stroke. The Framingham Heart Study provides valuable data for understanding CVD risk factors. This project aims to develop a classification model predicting the 10-year risk of Coronary Heart Disease (CHD) based on individual characteristics.

### Dataset Description
The dataset contains medical, behavioral, and demographic data on residents of Framingham, Massachusetts. Features include demographic factors, smoking status, medical history, and physiological metrics. The target variable is the 10-year risk of CHD.

### Feature Engineering and Data Pre-processing
The dataset undergoes extensive pre-processing to handle missing values, outliers, and feature manipulation. Techniques such as imputation, feature combination, and outlier trimming are employed. Iterations are conducted to test various pre-processing methods, ensuring robustness.

### Model Implementation
Seven machine learning models are implemented, including Logistic Regression, Decision Tree, and Random Forest. Hyperparameter tuning and cross-validation optimize model performance. Decision Tree emerges as the top performer.

### Model Evaluation
Recall score is chosen as the evaluation metric due to its relevance in identifying individuals at high risk of CVD. Decision Tree achieves the highest recall, indicating its effectiveness in predicting cardiovascular risk.

### Results
The Decision Tree model on the original dataset yields the best performance. Local and global explanations using SHaply Additive exPlanations (SHAP) provide insights into model predictions.

The provided summary statistics describe the performance of a machine learning model used to predict heart health indicators on a specific class, presumably representing a "healthy" or "non-event" outcome (indicated by label 0). Here's a detailed interpretation of the metrics:

The provided metrics reveal a notable discrepancy in the model's performance between the two classes. 
For class-0, the model demonstrates relatively high precision (0.86) and recall (0.92), indicating accurate predictions and a high sensitivity to instances of this class. The F1-score for class-0 (0.89) further supports this, suggesting a balanced performance between precision and recall. 

However, for class-1, the model's performance is considerably poorer. With a precision of 0.26 and a recall of 0.15, the model struggles to accurately predict instances of class-1, indicating a lower sensitivity and precision in identifying this class. 

The low F1-score for class-1 (0.19) underscores the challenge in achieving a balance between precision and recall for this class. Additionally, the support values highlight the class-1 instances as the minority class in the dataset, which could contribute to the model's difficulty in accurately predicting class-1. Overall, while the model performs reasonably well for class-0, there is a clear need for improvement in its ability to identify instances of class-1. 

Further exploration and optimization strategies may be necessary to enhance the model's performance, such as adjusting class weights, exploring alternative algorithms, or collecting additional data for class-1 to address the imbalance in the dataset.

### Conclusion
The project highlights the importance of data preprocessing, feature engineering, and model selection in developing accurate CVD risk prediction models. Decision Tree emerges as the most promising model, offering valuable insights for preventive healthcare strategies.

### Challenges Faced
Challenges include understanding complex medical features, handling missing values and outliers, and optimizing model parameters for performance and efficiency. Collaboration with medical professionals and iterative experimentation helped overcome these challenges.









