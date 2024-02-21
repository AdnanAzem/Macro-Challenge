# Macro-Challenge

### OverFlow
In this project we recieved 3 csv file: 

### Dataset
The dataset contains two columns:
<ol>
  <li>
    vba_code: contains a code that is written in vba.
  </li>
  <li>
    label: contains two values white or mal
  </li>
</ol>

### Data Preprocessing
<ul>
  <li>
    Basic and extended text cleaning for normalization.
  </li>
  <li>
    Handling of hexadecimal strings to address obfuscation.
  </li>
  <li>
    TF-IDF Vectorization: Applied with and without `max_features` to refine feature relevance.
  </li>
</ul>

### Features Extraction
We extract 4 more features from the dataset:
<ol>
  <li>character count</li>
  <li>lines count</li>
  <li>token count</li>
  <li>length of the maximum token</li>
</ol>

### Model Training
The dataset was splited for us we recived a train file for training the data and validation file for testing the data.<br>
We use a RandomForest Model to train the data with 2 prametres:
<ol>
  <li>n_estimators = 100</li>
  <li>random_state = 42</li>
</ol>

### Handling False Positives and Negatives
<ol>
  <li>Basic TF-IDF: 99.39% accuracy.</li>
  <li>TF-IDF with `max_features=1000`: 99.46% accuracy.</li>
  <li>Hexadecimal preprocessing: 99.51% accuracy.</li>
  <li>Addition of textual features: 99.62% accuracy.
</li>
</ol>

### Final Result:
<img src="https://github.com/AdnanAzem/Macro-Challenge/assets/88532380/fde5222d-23ba-4023-be02-1153d70f34aa">

### How to Run:
<ol>
  <li>Open CMD</li>
  <li>Run the command: python train.py</li>
  <li>Run the command: python inference.py</li>
</ol>
