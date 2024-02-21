# Macro-Challenge

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
