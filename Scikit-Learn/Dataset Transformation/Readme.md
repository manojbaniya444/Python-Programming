## Dataset Transformation

- [Custom Estimators](./custom_estimator.ipynb)
- [Feature Extraction](./Feature_Extraction.ipynb)
- [Preprocessing Data](./Preprocessing_Data.ipynb)

## Estimators

Object thata can learn from data has a fit method. It is **Estimator**. Example using algorightms it has a `.fit()` method. In scikit learn all these are `Estimators`. In sklearn not only **Algorithms** are estimators but any thing that **Learn From Data** are estimator. E.g `StandardScalar`, `Tokenizer`, `Vectorizer`,`PCA` etc.

There are two kinds of Estimators:

- Predictors : All machine learning algorithms which has `.predict()`.
- Transformers : Not a Prediction but transform data and has `.fit-transform()` and `.transform()` method.

---

## Custom Estimators

They are user defined classes that implement the scikit learn estimator interface. For modifying existing algorithms to entirely new algorithm developed for unique tasks.

There are some estimators which only has `.fit()` method. e.g **Clustering Algorithms**.
