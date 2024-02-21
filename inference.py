import pandas as pd
from model_utils import load_model, load_vectorizer, preprocess_data, extract_features

# Load the trained model and vectorizer
model = load_model('model/vba_code_mal_detection_rf_model.joblib')
vectorizer = load_vectorizer('model/vba_code_tfidf_vectorizer.joblib')

def predict(input_data):
    input_data_preprocessed = preprocess_data(input_data)
    input_features, _ = extract_features([input_data_preprocessed], vectorizer=vectorizer, mode='predict')
    prediction = model.predict(input_features)
    return prediction[0]

def batch_predict(csv_path):
    # Load and preprocess validation data
    print("loading data")
    validate_df = pd.read_csv(csv_path, encoding='utf-16-le', encoding_errors='ignore')
    validate_raw = validate_df.loc[:, 'vba_code'].values

    print("run batch prediction")
    predictions = [predict(code) for code in validate_raw]

    print("save prediction to csv")
    # save to prediction to csv
    test_prediction = pd.DataFrame(predictions, columns=['prediction'])
    test_prediction.to_csv('results/test_prediction.csv', index=False)
    return predictions

# Example of using the predict function
if __name__ == '__main__':
    # sample_input = 'Function SleekM()\nOn Error Resume Next\n   Select Case pinkk\n         Case 325\ndepositf = contingencyt\n            hackS = CDate(indexK)\n            CocosKeelingIslandsE = ToolsToolsH\n            usercentricY = Sgn(IncredibleWoodenBallO)\n         Case 166\n            challengeq = 994\n            TastyConcreteSaladm = CDbl(253)\nTunnelW = viralb\n            parsingV = Sin(depositR)\n         Case 395\nAssistantc = DynamicS\n            Marketings = Fix(BuckinghamshireR)\nmorphI = feedI\n            Softw = Round(561)\n            invoiceX = CoordinatorD\n      End Select\n   Select Case navigatei\n         Case 162\ndeliverc = Coordinatori\n            compellingz = CDate(hapticT)\n            neurald = leadingedgeM\n            calculater = Sgn(GrassrootsE)\n         Case 869\n            brandp = 411\n            Roadd = CDbl(223)\nAnalysta = paymenth\n            BarbadosDollarP = Sin(Pinel)\n         Case 701\ndepositP = Investorz\n            LegacyR = Fix(infrastructuresY)\nBooksToolsC = SleekMetalPantsA\nSub autoopen()\nFreshm = granularY - nichesT\nMassachusettsm = IntranetE - CambridgeshireP\nFranceT = ClothingToysAutomotiveT - R24783\nDownsizedk = LoopX - emarketsH\nMusicElectronicsGroceryP = MoneyMarketAccounth - Avonm\nSleekM\narrayw = pixelk - AgentR\nCentersW = IslandD - openarchitecturec\ntechnologiesS = portalst - navigatep\ninvoicej = PersonalLoanAccountL - parsingC\nhapticJ = TrinidadandTobagoDollarB - paradigmsp\nEnd Sub'
    # prediction = predict(sample_input)
    # print(f"Prediction: {prediction}")
    batch_predict('data/test_dataset_without_labels.csv')
