# Final-Project_Group5## Cardiovascular Disease Risk Prediction

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

### Conclusion
The project highlights the importance of data preprocessing, feature engineering, and model selection in developing accurate CVD risk prediction models. Decision Tree emerges as the most promising model, offering valuable insights for preventive healthcare strategies.

### Challenges Faced
Challenges include understanding complex medical features, handling missing values and outliers, and optimizing model parameters for performance and efficiency. Collaboration with medical professionals and iterative experimentation helped overcome these challenges.
