from sklearn.datasets import fetch_openml
#from dimensionality_reductions_jmsv.decomposition import PCA, TruncatedSVD
from sklearn.decomposition import PCA, TruncatedSVD
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle


# Load MNIST dataset
X, y  = fetch_openml(data_id=554, parser='auto', return_X_y=True) # https://www.openml.org/d/554
# Convert pandas dataframe to numpy array to avoid warning "valid feature names"
X = X.values
y = y.values

# Split into training and test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply PCA with 2 components
pca = PCA(n_components=50).fit(X_train)
X_train_pca = pca.transform(X_train)
X_test_pca = pca.transform(X_test)

# Train logistic regression on PCA reduced dataset
clf1 = LogisticRegression(random_state=0, max_iter=1000, solver='lbfgs', penalty='l2', n_jobs=5).fit(X_train_pca, y_train)

# Apply SVD with 2 components
svd = TruncatedSVD(n_components=50).fit(X_train)
X_train_svd = svd.transform(X_train)
X_test_svd = svd.transform(X_test)

# Train logistic regression on SVD reduced dataset
clf2 = LogisticRegression(random_state=0, max_iter=1000, solver='lbfgs', penalty='l2', n_jobs=5).fit(X_train_svd, y_train)

# save pickle file for each model
with open('log_regr_PCA.pkl', 'wb') as lr1:
    pickle.dump(clf1, lr1)

with open('log_regr_SVD.pkl', 'wb') as lr2:
    pickle.dump(clf2, lr2)

with open('dr_PCA.pkl', 'wb') as dr1:
    pickle.dump(pca, dr1)

with open('dr_SVD.pkl', 'wb') as dr2:
    pickle.dump(svd, dr2)