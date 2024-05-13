# README

## Setup and Running the Application Locally

To get the application running on your local machine, follow these steps:

### Prerequisites

- Docker
- Stable internet connection for downloading necessary data files

### Instructions

1. **Clone the repository:**

   ```
   git clone https://github.com/jasdeep06/assignment-kc.git
   ```

2. **Navigate to the project root directory:**

   ```
   cd assignment-kc
   ```

3. **Build the application using Docker Compose:**

   ```
   docker-compose build
   ```

4. **Start the application:**

   ```
   docker-compose up
   ```

   During the backend service initialization, a ~600MB `sessions.csv` file will be downloaded. Please ensure a stable internet connection during this setup phase.

5. **Access the application:**
   - Frontend is available at `http://localhost/`
   - Backend is available at `http://localhost:8000/`

A sample `test_user.csv` is available inside the `backend/test_data` folder in the repository, which you can use as a starting point.

## Tools, Libraries, and Frameworks

### Frontend

- **React**: Chosen for its flexibility and the extensive experience (5 years) I have working with it, React allows for building dynamic user interfaces with efficient data flow management across components.

### Backend

- **FastAPI**: Selected for its simplicity and efficiency, making it highly suitable for production environments.

### Libraries

- **scikit-learn**: Provides a comprehensive range of classifiers, regressors, and preprocessors, ideal for predictive analysis.
- **pandas**: An intuitive library for data manipulation, particularly with CSV files.

### Model

- **Random Forest Classifier**: Given the dataset's mix of categorical and numerical features, and the presence of many missing values, decision trees like Random Forest are well-suited. Although XGBoost could potentially yield better performance due to its strong track record in competitions, it requires extensive tuning that was not feasible within the project's time constraints.

### Preprocessing Techniques

Various vectorization and encoding techniques were utilized, including tf-idf vectorizer, count vectorizer, and one-hot encoding. Given the use of decision trees, which are robust to different feature scales, data scaling was not implemented.

### Feature Engineering

Focus was placed on aggregating features from `sessions.csv` to create new features. Techniques such as sum, mean, average, and count were employed. For detailed analysis, refer to `investigation.ipynb`.

## Roadmap for Future Improvements

1. **Optimization of Data Handling**: Improve inference speed by optimizing how session data is processed during predictions.
2. **Model Enhancement**: Implement and fine-tune an XGBoost model to improve prediction accuracy.
3. **Additional Data Utilization**: Integrate supplementary data from additional CSVs related to countries and age demographics to enhance feature engineering.
4. **Time Data Inclusion**: Incorporate time-related data previously omitted from `train_users_2.csv` into the predictive model.
5. **Error Handling**: Implement more robust error messaging in production.
6. **UI Enhancements**: Focus on improving the user interface aesthetics and functionality.
